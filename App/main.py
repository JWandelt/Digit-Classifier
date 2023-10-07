# Imports
import sys
import pygame
from pygame.locals import *

# Local imports
import App.Buttons as bt
import App.Buttons.SaveButton

pygame.init()

# Define constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (245, 245, 220)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (218, 160, 109)
SCREEN_WIDTH = 420
SCREEN_HEIGHT = 280

# Set variables.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
black_half = pygame.Rect(0, 0, SCREEN_WIDTH * 2/3, SCREEN_HEIGHT)
purple_half = pygame.Rect(SCREEN_WIDTH * 2/3, 0, SCREEN_WIDTH * 1/3, SCREEN_HEIGHT)
objects = []


def myFunction():
    print('Button Pressed')


# drawButton = App.Buttons.Button.Button(285, 25, 130, 67, screen, GREEN, 'Draw', myFunction)
saveButton = bt.SaveButton.SaveButton(285, 107, 130, 67, screen, BROWN, 'Save')
# clearButton = App.Buttons.Button.Button(285, 189, 130, 67, screen, RED, 'Clear', myFunction)


# objects.append(drawButton)
objects.append(saveButton)
# objects.append(clearButton)


def main():
    mouse_position = (0, 0)
    drawing = False
    screen.fill(BLACK, black_half)
    screen.fill(PURPLE, purple_half)
    pygame.display.set_caption("ScratchBoard")

    last_pos = None

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                if (drawing):
                    mouse_position = pygame.mouse.get_pos()
                    if last_pos is not None and mouse_position[0] < SCREEN_WIDTH * 2/3:
                        pygame.draw.line(screen, WHITE, last_pos, mouse_position, 20)
                    if mouse_position[0] < SCREEN_WIDTH * 2/3:
                        last_pos = mouse_position
            elif event.type == MOUSEBUTTONUP:
                last_pos = None
                drawing = False
            elif event.type == MOUSEBUTTONDOWN:
                drawing = True

        for o in objects:
            o.process()

        pygame.display.update()


if __name__ == "__main__":
    main()
