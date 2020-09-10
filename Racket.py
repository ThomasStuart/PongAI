import pygame

class Racket(object):

    def __init__(self, color, x, y, width, height, display):
        self.color  = color
        self.width  = width
        self.height = height
        self.x      = x
        self.y      = y

        #pygame.draw.rect(display, self.color, (self.x, self.y, self.width, self.height))
        self.rect = pygame.rect.Rect((self.x, self.y, self.width, self.height))
        pygame.draw.rect(display, self.color, self.rect)

    def moveUp(self):
        self.rect.move_ip(0, -1)

    def moveDown(self):
        self.rect.move_ip(0, 1)

    def draw(self, display):
        pygame.draw.rect(display, self.color, self.rect )