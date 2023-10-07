# Imports
import sys
import pygame
from pygame.locals import *

# Local imports
import App.Button

pygame.init()

screen = pygame.display.set_mode((420, 280), 0, 32)
font = pygame.font.SysFont('Arial', 40)
objects = []

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (245, 245, 220)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (218, 160, 109)

black_half = pygame.Rect(0, 0, 280, 280)
purple_half = pygame.Rect(280, 0, 140, 280)

def myFunction():
    print('Button Pressed')


drawButton = App.Button.Button(285, 25, 130, 67, screen, GREEN, 'Draw', myFunction)
saveButton = App.Button.Button(285, 107, 130, 67, screen, BROWN, 'Save', myFunction, True)
clearButton = App.Button.Button(285, 189, 130, 67, screen, RED, 'Clear', myFunction, True)


objects.append(drawButton)
objects.append(saveButton)
objects.append(clearButton)


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
                    if last_pos is not None:
                        pygame.draw.line(screen, WHITE, last_pos, mouse_position, 3)
                    last_pos = mouse_position
            elif event.type == MOUSEBUTTONUP:
                mouse_position = (0, 0)
                drawing = False
            elif event.type == MOUSEBUTTONDOWN:
                drawing = True

        for object in objects:
            object.process()

        pygame.display.update()


if __name__ == "__main__":
    main()
