import pygame
import Constants
import Colors
from AngledLine import AngledLine

class Player(object):

    def __init__(self, color, x, y, width, height, display, isHuman):
        self.color  = color
        self.width  = width
        self.height = height
        self.x      = x
        self.y      = y
        self.dy     = 0
        self.display = display
        self.score   = 0
        self.isHuman = isHuman
        self.redirectLines = []
        pygame.draw.rect(self.display, self.color, (self.x, self.y, self.width, self.height))
        self.drawRedirectLines()

    def moveUp(self ):
        self.dy = -10
        self.y -= 10

    def moveDown(self):
        self.dy = 10
        self.y += 10

    def draw(self):
        pygame.draw.rect(self.display, self.color, (self.x, self.y, self.width, self.height))
        self.reRenderRedirectLines()

    def drawRedirectLines(self):
        y  = self.y + 10
        offset     = 0
        angle      = -110

        if not self.isHuman:
            offset     = Constants.RACKET_WIDTH
            angle      = -70

        # 180 degrees of redirection from either side
        for i in range(Constants.NUM_RACKET_REDIRECT_ANGLES):
            self.redirectLines.append( AngledLine(Colors.NEON, self.x + offset, y, angle, 20, 2, self.display) )
            y     += Constants.DISTANCE_BETWEEN_REDIRECT
            if self.isHuman:
                angle -= Constants.ANGLE_CHANGE
            else:
                angle += Constants.ANGLE_CHANGE

    def reRenderRedirectLines(self):
        for i in range(Constants.NUM_RACKET_REDIRECT_ANGLES):
            self.redirectLines[i].moveLine(0, self.dy)


    def getRedirectAngle(self, ballYPosition):
        positionOnRacket = ballYPosition - self.y
        if    ballYPosition < self.y + Constants.RACKET_HALF_HEIGHT:
            return 70 - ((positionOnRacket / Constants.RACKET_HALF_HEIGHT) * 70)
        elif  ballYPosition > self.y + Constants.RACKET_HALF_HEIGHT:
            return -1 * (70 - (((positionOnRacket - 70) / Constants.RACKET_HALF_HEIGHT) * 70))
        else:
            return 0