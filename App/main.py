import sys

import pygame
from pygame.locals import *

import App.Button

pygame.init()

screen = pygame.display.set_mode((1000, 1000), 0, 32)
font = pygame.font.SysFont('Arial', 40)
objects = []

def myFunction():
    print('Button Pressed')

customButton = App.Button.Button(30, 30, 400, 100, screen, 'Button One (onePress)', myFunction)
customButton2 = App.Button.Button(30, 140, 400, 100, screen, 'Button Two (multiPress)', myFunction, True)

objects.append(customButton)
objects.append(customButton2)

def main():
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    mouse_position = (0, 0)
    drawing = False
    screen.fill(BLACK)
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
