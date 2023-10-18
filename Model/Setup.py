import os.path
from tensorflow import keras
from sklearn.metrics import classification_report
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot_learning_curve(history):
    # Extract training and validation accuracy and loss from the history object
    training_accuracy = history.history['accuracy']
    validation_accuracy = history.history['val_accuracy']
    training_loss = history.history['loss']
    validation_loss = history.history['val_loss']

    # Create subplots
    plt.figure(figsize=(12, 4))

    # Plot Training and Validation Accuracy
    plt.subplot(1, 2, 1)
    plt.plot(training_accuracy, label='Training Accuracy')
    plt.plot(validation_accuracy, label='Validation Accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.title('Training and Validation Accuracy')
    plt.legend()

    # Plot Training and Validation Loss
    plt.subplot(1, 2, 2)
    plt.plot(training_loss, label='Training Loss')
    plt.plot(validation_loss, label='Validation Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.title('Training and Validation Loss')
    plt.legend()

    # Show the plot
    plt.tight_layout()
    plt.show()


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
    learning_history = model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))

    # Make prediction from test data
    prediction_probability = model.predict(x_test)
    prediction = np.array([np.argmax(pred) for pred in prediction_probability])

    # Display the model performance
    print(classification_report(y_test, prediction))

    # Save model
    model.save('mnist_classification.h5')
    plot_learning_curve(learning_history)

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
