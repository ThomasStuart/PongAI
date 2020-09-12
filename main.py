# Import and initialize the pygame library
import pygame
from MovingObjects.Player import Player
from MovingObjects.PongBall import PongBall
from Border import Border
from AngledLine import*
from MovingObjects.EventManager import*
import Colors
import Constants

def text_objects(text, font):
    textSurface = font.render(text, True, Colors.BLACK)
    return textSurface, textSurface.get_rect()

def message_display(text, x, y, gameDisplay):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)

def display_score(computerPlayer, humanPlayer, gameDisplay):
    message_display( str(computerPlayer.score), Constants.COMPUTER_SCORE_X, Constants.SCORE_Y, gameDisplay)
    message_display( str(humanPlayer.score),    Constants.HUMAN_SCORE_X,    Constants.SCORE_Y, gameDisplay)

pygame.init()

# Set up the drawing window
display = pygame.display.set_mode([Constants.DISPLAY_WIDTH, Constants.DISPLAY_HEIGHT])
# Fill the background with white
display.fill(Colors.WHITE)

#GeneratePlayers
ComputerPlayer = Player(Colors.BLUE, Constants.RACKET_OFFSET, Constants.RACKET_START_HEIGHT, Constants.RACKET_WIDTH,
                        Constants.RACKET_HEIGHT, display, False)

HumanPlayer = Player(Colors.BLUE, Constants.DISPLAY_WIDTH - Constants.RACKET_OFFSET - Constants.RACKET_WIDTH,
                     Constants.RACKET_START_HEIGHT, Constants.RACKET_WIDTH, Constants.RACKET_HEIGHT, display, True)

Ball   = PongBall(Colors.RED, Constants.PONG_START_X, Constants.PONG_START_Y, Constants.PONG_RADIUS, display)
Border = Border(Constants.BORDER_X, Constants.BORDER_Y)

Grid  = EventManager(ComputerPlayer, HumanPlayer, Ball, display)
# Run until the user asks to quit
FPS = 25
clock = pygame.time.Clock()
running = True
pressed_up   = False
pressed_down = False



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
    else:
        ComputerPlayer.dy = 0
        HumanPlayer.dy    = 0

    # # if player hits the pong ball, redirect the ball
    # Grid.check_collision()
    # # if pong ball hits a wall, add score to player
    # Grid.check_score()# if player won, stop game

    #Update all elements
    # First, erase the display and repaint white
    display.fill(Colors.WHITE)
    # Second, draw on next frame
    HumanPlayer.draw()
    ComputerPlayer.draw()
    Border.draw(display)
    Grid.checkEvents()
    Ball.updatePosition()
    display_score(ComputerPlayer, HumanPlayer, display)

    # update the display with the new changes
    pygame.display.update()
    # - FPS - keep the same speed on all computers -
    clock.tick(FPS)

# Done! Time to quit.
pygame.quit()




