"""
My Awesome Picture

This is a simple Pygame template that demonstrates basic graphics rendering
and event handling, including shapes, text, and basic user input handling.
The game loop updates and draws objects on the screen and listens for the
QUIT event to exit the game.

Written by: Your Name
Date: YYYY-MM-DD
"""

# Imports
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Set up display
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CAPTION = "My Awesome Picture"
FPS = 60

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption(CAPTION)

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (150, 0, 150)
ORANGE = (255, 125, 0)

# Fonts
FONT_SM = pygame.font.Font(None, 48)
FONT_MD = pygame.font.Font(None, 64)
FONT_LG = pygame.font.Font(None, 96)

# Game functions
def process_input():
    """Handle user input events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


def update():
    """Update game logic (e.g., movement, game state changes)."""
    pass


def draw():
    """Draw everything to the screen."""
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, [50, 50, 400, 300])
    pygame.draw.line(screen, GREEN, [300, 40], [100, 500], 10)
    pygame.draw.ellipse(screen, BLUE, [100, 100, 600, 300], 2)
    pygame.draw.polygon(screen, PURPLE, [[300, 200],
                                         [150, 400],
                                         [700, 500]])

    # Angles for arcs are measured in radians (a pre-cal topic)
    pygame.draw.arc(screen, BLACK, [100, 100, 300, 200], 0, math.pi / 2, 5)

    # Put text on the screen
    text1 = FONT_SM.render("When you first learn Pygame", True, BLACK)
    text2 = FONT_LG.render("Bottom Text", True, ORANGE)
    screen.blit(text1, [200, 50])
    screen.blit(text2, [100, 500])


def game_loop():
    """Main game loop."""
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
