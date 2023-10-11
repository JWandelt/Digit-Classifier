import pygame.image
import App.Buttons.Button as bt

# Define constants
SCREEN_WIDTH = 420
DESIRED_WIDTH = SCREEN_WIDTH * 2 / 3
SCREEN_HEIGHT = 280
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
black_half = pygame.Rect(0, 0, SCREEN_WIDTH * 2 / 3, SCREEN_HEIGHT)


class DrawEraseButton(bt.Button):
    def function(self, arg):
        if arg[0] == WHITE:
            arg[0] = BLACK
        else:
            arg[0] = WHITE
