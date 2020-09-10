# Import and initialize the pygame library
import Colors
import Constants
import pygame
from Racket   import Racket
from PongBall import PongBall


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



# PongBall = pygame.draw.circle(display, Colors.RED, (Constants.PONG_START_X, Constants.PONG_START_Y), Constants.PONG_RADIUS)
Ball = PongBall(Colors.RED, Constants.PONG_START_X, Constants.PONG_START_Y, Constants.PONG_RADIUS, display)

# Run until the user asks to quit
running = True
while running:


    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                HumanPlayer.moveUp()
            if event.key == pygame.K_DOWN:
                HumanPlayer.moveDown()

    # move the computer
    # move the ball

    # if player hits the pong ball, redirect
    # if pong ball hits a wall, add score to player
        # reset the ball

    # if player won, stop game
    display.fill(Colors.WHITE)
    HumanPlayer.draw(display)
    Ball.move(display)
    pygame.display.update()

# Done! Time to quit.
pygame.quit()