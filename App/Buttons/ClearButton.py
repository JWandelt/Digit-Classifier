import pygame.image
import App.Buttons.Button as bt

# Define constants
SCREEN_WIDTH = 420
DESIRED_WIDTH = SCREEN_WIDTH * 2 / 3
SCREEN_HEIGHT = 280
BLACK = (0, 0, 0)
black_half = pygame.Rect(0, 0, SCREEN_WIDTH * 2 / 3, SCREEN_HEIGHT)


class ClearButton(bt.Button):
    def function(self, arg):
        self.screen.fill(BLACK, black_half)
