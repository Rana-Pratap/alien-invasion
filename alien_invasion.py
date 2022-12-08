import pygame
import sys
from pygame.locals import *
from settings import Settings
from ship import Ship


def run():
    # Initialise game and create a screen object
    pygame.init()
    window = Settings()
    screen = pygame.display.set_mode((window.width, window.height))
    
    # Set the title of window
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(screen)

    # Start the main loop for the game
    running = True
    while running:

        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            '''This can also work with Esc button
             if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                sys.exit()
            '''   
        # Set background color, redraw the screen after every event through the loop
        screen.fill(window.bg_color)

        ship.blitme()

        # Make the most recently drawn screen visible
        pygame.display.flip()

run()