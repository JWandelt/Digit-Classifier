import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class TextBox():
    def __init__(self, x, y, width, height, screen, text, textBoxColor='#ffffff', textColor=WHITE):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font = pygame.font.SysFont('Arial', 15)
        self.textColor = textColor

        self.fillColors = {
            'normal': textBoxColor
        }

        self.textBoxSurface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.textBoxRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.screen = screen

    def displayText(self):
        pygame.draw.rect(self.textBoxSurface, pygame.Color(self.fillColors['normal']), (0, 0, self.width, self.height),
                         border_radius=20)

        textBoxSurf = self.font.render(self.text, True, self.textColor)

        self.textBoxSurface.blit(textBoxSurf, [
            self.width / 2 - textBoxSurf.get_rect().width / 2,
            self.height / 2 - textBoxSurf.get_rect().height / 2
        ])
        self.screen.blit(self.textBoxSurface, self.textBoxRect)