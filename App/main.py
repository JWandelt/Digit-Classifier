# Imports
import sys
import pygame
from pygame.locals import *

# Local imports
from App.Buttons import ClearButton, DrawEraseButton, SaveButton

pygame.init()

# Define constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BROWN = (245, 245, 220)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (218, 160, 109)
SCREEN_WIDTH = 420
SCREEN_HEIGHT = 280

# Set variables.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
black_half = pygame.Rect(0, 0, SCREEN_WIDTH * 2/3, SCREEN_HEIGHT)
lb_half = pygame.Rect(SCREEN_WIDTH * 2 / 3, 0, SCREEN_WIDTH * 1 / 3, SCREEN_HEIGHT)
drawing_color = [WHITE]
objects = []

# Define buttons.
drawButton = DrawEraseButton.DrawEraseButton(285, 25, 130, 67, screen, GREEN, 'Draw/Erase', drawing_color)
saveButton = SaveButton.SaveButton(285, 107, 130, 67, screen, BROWN, 'Save')
clearButton = ClearButton.ClearButton(285, 189, 130, 67, screen, RED, 'Clear')

objects.append(drawButton)
objects.append(saveButton)
objects.append(clearButton)


def main():
    drawing = False
    screen.fill(BLACK, black_half)
    screen.fill(LIGHT_BROWN, lb_half)
    pygame.display.set_caption("ScratchBoard")

    last_pos = None

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                if drawing:
                    mouse_position = pygame.mouse.get_pos()
                    if last_pos is not None and mouse_position[0] < SCREEN_WIDTH * 2/3:
                        pygame.draw.line(screen, drawing_color[0], last_pos, mouse_position, 20)
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
