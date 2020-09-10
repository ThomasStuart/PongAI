import pygame

class PongBall(object):

    def __init__(self, color, x, y, radius, display):
        self.color  = color
        self.radius  = radius
        self.x      = x
        self.y      = y

        self.circle = pygame.draw.circle(display, self.color, (self.x, self.y), self.radius )

    def moveLeft(self):
        self.rect.move_ip(1, 0)

    def moveRight(self):
        self.rect.move_ip(-1, 0)

    def draw(self, display):
        pygame.draw.rect(display, self.color, self.rect )


    def move(self, display):
        self.x += 10
        pygame.draw.circle(display, self.color, (self.x , self.y), self.radius )