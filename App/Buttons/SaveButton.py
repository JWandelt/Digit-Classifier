import pygame.image
import cv2
import App.Buttons.Button as bt

# Define constants
SCREEN_WIDTH = 420
DESIRED_WIDTH = SCREEN_WIDTH * 2/3
SCREEN_HEIGHT = 280

class SaveButton(bt.Button):
    def function(self):
        pygame.image.save(self.screen, "screenshot.jpg")
        image = cv2.imread("screenshot.jpg")

        # Processing the image
        image = image[0:280, 0:280]
        image = cv2.resize(image, (28, 28), interpolation = cv2.INTER_AREA)
        cv2.imwrite("model_input2.jpg", image)
