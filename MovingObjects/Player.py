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
        self.dy = -Constants.RACKET_SPEED
        self.y -= Constants.RACKET_SPEED

    def moveDown(self):
        self.dy = Constants.RACKET_SPEED
        self.y += Constants.RACKET_SPEED

    def draw(self):
        pygame.draw.rect(self.display, self.color, (self.x, self.y, self.width, self.height))
        self.reRenderRedirectLines()

    def drawRedirectLines(self):
        y      = self.y + 10
        offset = 0
        angle  = Constants.COMPUTER_REDIRECT_START

        if not self.isHuman:
            offset     = Constants.RACKET_WIDTH
            angle      = -1 * Constants.MAX_REDIRECT_ANGLE

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
        print(positionOnRacket)
        if    ballYPosition < self.y + Constants.RACKET_HALF_HEIGHT:
            return Constants.MAX_REDIRECT_ANGLE - ((positionOnRacket / Constants.RACKET_HALF_HEIGHT) * Constants.MAX_REDIRECT_ANGLE)
        elif  ballYPosition > self.y + Constants.RACKET_HALF_HEIGHT:
            return -1 *  (((positionOnRacket - Constants.RACKET_HALF_HEIGHT) / Constants.RACKET_HALF_HEIGHT) * Constants.MAX_REDIRECT_ANGLE)
        else:
            return 0