import keras.models
import numpy as np
import pygame.image
import cv2
import App.Buttons.Button as bt
from App.Misc import TextBox

# Define constants
SCREEN_WIDTH = 420
DESIRED_WIDTH = SCREEN_WIDTH * 2/3
SCREEN_HEIGHT = 280
BLACK = (0, 0, 0)
LIGHT_BROWN = (245, 245, 220)
black_half = pygame.Rect(0, 0, SCREEN_WIDTH * 2 / 3, SCREEN_HEIGHT)

class PredictButton(bt.Button):
    prediction = ""
    def function(self, arg):
        pygame.image.save(self.screen, "screenshot.jpg")
        image = cv2.imread("screenshot.jpg")

        # Processing the image
        image = image[0:280, 0:280]
        image = cv2.resize(image, (28, 28), interpolation = cv2.INTER_LINEAR)
        cv2.imwrite("model_input.jpg", image)
        self.screen.fill(BLACK, black_half)

        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = np.expand_dims(image, axis=0)

        model = keras.models.load_model('../Model/mnist_classification.h5')
        self.prediction = np.argmax(model.predict(image))
