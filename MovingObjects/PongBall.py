import pygame
import math
import Constants
import random
import Arrow

class PongBall(object):

    def __init__(self, color, x, y, radius, display):
        self.color  = color
        self.radius  = radius
        self.x      = x
        self.y      = y
        self.dir    = 1
        self.dx     = 20
        self.dy     = 0

        self.display = display
        self.circle = pygame.draw.circle(display, self.color, (self.x, self.y), self.radius )
        #self.arrow  = Arrow()

    # def move(self):
    #     self.x += 20 * self.dir
    #     pygame.draw.circle(self.display, self.color, (self.x , self.y), self.radius )

    def flipDir(self):
        self.dir = -1 * self.dir


    def updatePosition(self):
        self.x +=  self.dx * self.dir
        self.y +=  self.dy
        pygame.draw.circle(self.display, self.color, (self.x, self.y), self.radius)


    def reset(self):
        self.x = Constants.PONG_START_X
        self.y = Constants.PONG_START_Y
        self.dy = 0
        self.dir = -1 if random.randint(0,1) == 0 else 1
