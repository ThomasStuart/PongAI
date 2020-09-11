# Import and initialize the pygame library
import Colors
import Constants
import math
import pygame
from MovingObjects.Racket import Racket
from MovingObjects.PongBall import PongBall
from Border import Border

def text_objects(text, font):
    textSurface = font.render(text, True, Colors.BLACK)
    return textSurface, textSurface.get_rect()

def message_display(text, gameDisplay):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((Constants.DISPLAY_WIDTH/2),(50))
    gameDisplay.blit(TextSurf, TextRect)


pygame.init()

# Set up the drawing window
display = pygame.display.set_mode([Constants.DISPLAY_WIDTH, Constants.DISPLAY_HEIGHT])
# Fill the background with white
display.fill(Colors.WHITE)

#GeneratePlayers
ComputerPlayer = Racket(Colors.BLUE, Constants.RACKET_OFFSET, Constants.RACKET_START_HEIGHT, Constants.RACKET_WIDTH,
                      Constants.RACKET_HEIGHT, display)

HumanPlayer = Racket(Colors.BLUE, Constants.DISPLAY_WIDTH - Constants.RACKET_OFFSET - Constants.RACKET_WIDTH ,
                    Constants.RACKET_START_HEIGHT, Constants.RACKET_WIDTH, Constants.RACKET_HEIGHT, display)

Ball   = PongBall(Colors.RED, Constants.PONG_START_X, Constants.PONG_START_Y, Constants.PONG_RADIUS, display)
Border = Border(Constants.BORDER_X, Constants.BORDER_Y)

# Run until the user asks to quit
FPS = 25
clock = pygame.time.Clock()
running = True
pressed_up   = False
pressed_down = False

start_pos = (100,100)
radar_len = 15
#x = radar[0] + math.cos(math.radians(135)) * radar_len
#y = radar[1] + math.sin(math.radians(135)) * radar_len

while running:
    #Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:    # check for key presses
            if event.key == pygame.K_SPACE:
                Ball =  PongBall(Colors.RED, Constants.PONG_START_X, Constants.PONG_START_Y, Constants.PONG_RADIUS, display)
            if event.key == pygame.K_UP:      # up arrow goes up
                pressed_up = True
            elif event.key == pygame.K_DOWN:  # down arrow goes down
                pressed_down = True
        elif event.type == pygame.KEYUP:      # check for key releases
            if event.key == pygame.K_UP:      # up arrow goes up
                pressed_up = False
            elif event.key == pygame.K_DOWN:  # down arrow goes down
                pressed_down = False

    if pressed_up:
        ComputerPlayer.moveUp()
        HumanPlayer.moveUp()
    elif pressed_down:
        ComputerPlayer.moveDown()
        HumanPlayer.moveDown()

    # move the computer
    # move the ball

    # if player hits the pong ball, redirect
    # if pong ball hits a wall, add score to player
        # reset the ball

    # if player won, stop game
    display.fill(Colors.WHITE)
    if Ball.collision(HumanPlayer.x, HumanPlayer.y, HumanPlayer.width, HumanPlayer.height, Ball.x, Ball.y, Ball.radius) or Ball.collision(ComputerPlayer.x, ComputerPlayer.y, ComputerPlayer.width, ComputerPlayer.height, Ball.x, Ball.y, Ball.radius):
        print("True")
        Ball.flipDir()

    HumanPlayer.draw()
    ComputerPlayer.draw()
    Ball.move(display)
    message_display("Score", display)
    Border.draw(display)
    #pygame.draw.line(display, Colors.BLUE, radar, (x, y), 1)
    pygame.display.update()
    # - FPS - keep the same speed on all computers -
    clock.tick(FPS)

# Done! Time to quit.
pygame.quit()




