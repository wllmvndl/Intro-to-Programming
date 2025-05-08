"""
This is not my code. It was a templete provided to me by Jon Cooper. 
"""

# Imports
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Set up display
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720
CAPTION = "Window Title"
FPS = 60

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption(CAPTION)

# Game functions
def process_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


def update():
    pass


def draw():
    pass


def game_loop():
    clock = pygame.time.Clock()

    running = True
    while running:
        running = process_input()
        update()
        draw()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    game_loop()
