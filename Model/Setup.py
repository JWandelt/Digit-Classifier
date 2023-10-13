import os.path
from tensorflow import keras
from sklearn.metrics import classification_report
import numpy as np


def train_model():
    # Load data provided by keras
    data = keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = data.load_data()

    # Normalize the input data to the range [0, 1]
    x_train, x_test = x_train / 255.0, x_test / 255.0

    # Create a model using the Sequential API
    model = keras.Sequential([
        # Convolutional Layers
        keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        keras.layers.MaxPooling2D((2, 2)),
        keras.layers.Conv2D(64, (3, 3), activation='relu'),
        keras.layers.MaxPooling2D((2, 2)),

        # Flatten the output of the convolutional layers
        keras.layers.Flatten(),

        # Fully Connected Layers
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dropout(0.5),

        # Output Layer
        keras.layers.Dense(10, activation='softmax')
    ])

    # Compile the model
    model.compile(
        optimizer=keras.optimizers.Adam(),
        loss=keras.losses.SparseCategoricalCrossentropy(),
        metrics=['accuracy']
    )

    # Reshape the input data to include a single channel (since MNIST images are grayscale)
    x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
    x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)

    # Train the model
    model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

    # Make prediction from test data
    prediction_probability = model.predict(x_test)
    prediction = np.array([np.argmax(pred) for pred in prediction_probability])

    # Display the model performance
    print(classification_report(y_test, prediction))

    # Save model
    model.save('mnist_classification.h5')


path = 'mnist_classification.h5'

file_exists = os.path.isfile(path)

if file_exists:
    print("Model already present. Skipping training.")
else:
    print("No model present. Building it right now.")

    train_model()
    file_exists = os.path.isfile(path)

    if file_exists:
        print("Model successfully trained. You can now use the digit classifier.")
    else:
        print("Something went wrong durin the training process.")
