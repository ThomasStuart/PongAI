import pygame

class Racket(object):

    def __init__(self, color, x, y, width, height, display):
        self.color  = color
        self.width  = width
        self.height = height
        self.x      = x
        self.y      = y
        self.display = display
        pygame.draw.rect(self.display, self.color, (self.x, self.y, self.width, self.height))

    def moveUp(self ):
        self.y -= 10

    def moveDown(self):
        self.y += 10

    def draw(self):
        pygame.draw.rect(self.display, self.color, (self.x, self.y, self.width, self.height))