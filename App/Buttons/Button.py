import pygame
from abc import ABC, abstractmethod


class Button(ABC):
    def __init__(self, x, y, width, height, screen, buttonColor='#ffffff', buttonText='Button',
                 onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False
        font = pygame.font.SysFont('Arial', 40)

        self.fillColors = {
            'normal': buttonColor,
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

        self.alreadyPressed = False
        self.screen = screen

    def process(self):
        mousePos = pygame.mouse.get_pos()

        # Draw a rounded rectangle as the button background
        pygame.draw.rect(self.buttonSurface, pygame.Color(self.fillColors['normal']), (0, 0, self.width, self.height),
                         border_radius=20)

        if self.buttonRect.collidepoint(mousePos):
            pygame.draw.rect(self.buttonSurface, pygame.Color(self.fillColors['hover']),
                             (0, 0, self.width, self.height), border_radius=20)

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                pygame.draw.rect(self.buttonSurface, pygame.Color(self.fillColors['pressed']),
                                 (0, 0, self.width, self.height), border_radius=20)

                if self.onePress:
                    self.function()

                elif not self.alreadyPressed:
                    self.function()
                    self.alreadyPressed = True

            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        self.screen.blit(self.buttonSurface, self.buttonRect)

    @abstractmethod
    def function(self):
        pass
