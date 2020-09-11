import pygame
import Colors
import Constants

class Border:

    def __init__(self, startX, startY):
        self.x = startX
        self.y = startY

    def draw(self, display):
        offset = Constants.BORDER_HEIGHT + 100

        for i in range(8):
            pygame.draw.rect(display, Colors.BLACK, (self.x, ( (i  * Constants.BORDER_HEIGHT) + (i * offset)), Constants.BORDER_WIDTH, Constants.BORDER_HEIGHT))