import pygame
import math
from AngledLine import AngledLine
import Colors


class Arrow:

    def __init__(self, color, start_x, start_y, angleM, angleB, length, display):
        self.color   = color
        self.start_x = start_x
        self.start_y = start_y
        self.length  = length
        self.display = display
        self.mainLine   = AngledLine(Colors.NEON, start_x, start_y,   angleM,   length, 2, display)
        self.topBack    = AngledLine(Colors.NEON, start_x, start_y,   angleB, length/4, 2, display)
        self.bottomBack = AngledLine(Colors.NEON, start_x, start_y,  -angleB, length/4, 2, display)
        # pygame.draw.line(self.display, self.color, (self.start_x, self.start_y), (self.end_x, self.end_y), self.length)
        # pygame.draw.line(self.display, self.color, (self.end_x, self.end_y), (self.end_x , self.end_y), self.length/4)
        # pygame.draw.line(self.display, self.color, (self.end_x, self.end_y), (self.end_x, self.end_y), self.length/4)


    def move(self, x, y):
        pass