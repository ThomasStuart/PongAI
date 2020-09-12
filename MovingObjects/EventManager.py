import pygame
import Constants
import math
from MovingObjects.Player import Player
from MovingObjects.PongBall import PongBall

class EventManager:

    def __init__(self, computer, human, ball, display):
        self.computer = computer
        self.human    = human
        self.ball     = ball
        self.display  = display

    def checkEvents(self):
        self.check_score()
        self.check_collision()
        self.check_off_grid()

    def check_off_grid(self):
        if self.ball.y <= 0 or self.ball.y >= Constants.DISPLAY_HEIGHT:
            self.ball.dy *= -1

    def check_score(self):
        # if pong ball hits a wall, add score to player
        if self.ball.x < Constants.WALL_SCORE_LEFT:
            self.human.score += 1
            self.ball.reset()
        elif self.ball.x > Constants.WALL_SCORE_RIGHT:
            self.computer.score += 1
            self.ball.reset()

    def check_collision(self):
        if self.collision(self.computer,self.ball):
            self.redirect(self.computer)
        elif  self.collision(self.human, self.ball):
            self.redirect(self.human)


    def collision(self, rect, ball):
        rleft, rtop, width, height   = rect.x, rect.y, Constants.RACKET_WIDTH, Constants.RACKET_HEIGHT # rectangle definition
        center_x, center_y, radius   = ball.x, ball.y, Constants.PONG_RADIUS                           # circle definition
        # complete boundbox of the rectangle
        rright, rbottom = rleft + width, rtop + height

        # bounding box of the circle
        cleft, ctop = center_x - radius, center_y - radius
        cright, cbottom = center_x + radius, center_y + radius

        # trivial reject if bounding boxes do not intersect
        if rright < cleft or rleft > cright or rbottom < ctop or rtop > cbottom:
            return False  # no collision possible

        # check whether any point of rectangle is inside circle's radius
        for x in (rleft, rleft + width):
            for y in (rtop, rtop + height):
                # compare distance between circle's center point and each point of
                # the rectangle with the circle's radius
                if math.hypot(x - center_x, y - center_y) <= radius:
                    return True  # collision detected

        # check if center of circle is inside rectangle
        if rleft <= center_x <= rright and rtop <= center_y <= rbottom:
            return True  # overlaid

        return False  # no collision detected



    def redirect(self, rect):
        # get angle hit on the racket
        redirectAngle = rect.getRedirectAngle(self.ball.y)
        print("ball @ (", self.ball.x , ",", self.ball.y , ") -> rediret angle= ", redirectAngle, end="")
        # do NOT change the DX speed of the ball. IT SHOULD NEVER CHANGE!!
        self.ball.dy = Constants.PONG_SPEED * (redirectAngle / Constants.MAX_REDIRECT_ANGLE)
        self.ball.dy = abs(self.ball.dy ) if redirectAngle < 0.00 else -1 * abs(self.ball.dy)
        self.ball.flipDir()
        print(",  dx= ", self.ball.dx, ",  ball dy=", self.ball.dy )