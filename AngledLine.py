import pygame
import math

class AngledLine:

    def __init__(self, color, start_x, start_y, angle, length, width, display):
        self.color   = color
        self.start_x = start_x
        self.start_y = start_y
        self.end_x   = (start_x + math.cos(math.radians(angle)) * length)
        self.end_y   = (start_y + math.sin(math.radians(angle)) * length)
        self.length  = length
        self.width   = width
        self.display = display
        pygame.draw.line(self.display, self.color, (self.start_x, self.start_y), (self.end_x, self.end_y), self.width)

    # def draw(self):
    #     pygame.draw.line(self.display, self.color, (self.start_x, self.start_y), (self.end_x, self.end_y), self.width)

    def moveLine(self, dx, dy):
        self.start_x += dx
        self.start_y += dy
        self.end_x   += dx
        self.end_y   += dy
        pygame.draw.line(self.display, self.color, (self.start_x, self.start_y), (self.end_x, self.end_y), self.width)