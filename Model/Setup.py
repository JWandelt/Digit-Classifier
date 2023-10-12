import os.path
from tensorflow import keras
from sklearn.metrics import classification_report
import numpy as np


def train_model():
    # Load data provided by keras
    data = keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = data.load_data()

    # Create model using sequential API
    model = keras.Sequential([
        # Input Layers
        keras.layers.Flatten(input_shape=(28, 28,)),
        # Hidden Layers
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dropout(0.5),
        # Output Layers
        keras.layers.Dense(10, activation='softmax')
    ])

    # Compile model
    model.compile(
        optimizer=keras.optimizers.Adam(),
        loss=keras.losses.SparseCategoricalCrossentropy(),
        metrics=['accuracy']
    )

    # Model training
    model.fit(x_train, y_train, verbose=1, epochs=48, batch_size=32)

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
