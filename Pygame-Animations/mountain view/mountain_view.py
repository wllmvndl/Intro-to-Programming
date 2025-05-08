"""
My Awesome Picture

This is a simple Pygame template that demonstrates basic graphics rendering
and event handling, including shapes, text, and basic user input handling.
The game loop updates and draws objects on the screen and listens for the
QUIT event to exit the game.

Written by: William Vandale
Date: 2025 Feburary 27
"""

# Imports
import math
import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up display
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
CAPTION = "Mountian View"
FPS = 60

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption(CAPTION)

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 100)
BLACK = (0, 0, 0)
DARK_BLUE = (0, 0, 10)
PURPLE = (150, 0, 150)
ORANGE = (255, 125, 0)

# Fonts
FONT_SM = pygame.font.Font(None, 24)
FONT_MD = pygame.font.Font(None, 64)
FONT_LG = pygame.font.Font(None, 96)

# Sounds
birds_chirping_music = 'assets/music/birds_chirping.ogg'
pygame.mixer.music.load(birds_chirping_music)

# Draw Functions

def draw_sky():
    pygame.draw.rect(screen, (70, 90, 230), [0, 180, 1280, 180])
    pygame.draw.rect(screen, (130, 160, 240), [0, 360, 1280, 180])


def draw_moon():
    pygame.draw.ellipse(screen, (180, 200, 250), [990, 190, 80, 80])
    pygame.draw.ellipse(screen, (70, 90, 230), [975, 175, 85, 85])
    pygame.draw.rect(screen, (50, 80, 170), [0, 0, 1280, 180])
    

def draw_mountains():
    pygame.draw.polygon(screen, (80, 140, 170), [[0, 500], [330, 410], [1280, 650]])
    pygame.draw.polygon(screen, (50, 120, 120), [[0, 430], [800, 530], [0, 720]])
    
    pygame.draw.polygon(screen, (40, 120, 80), [[0, 520], [1280, 200], [1280, 720], [0, 720]])
    
    pygame.draw.polygon(screen, (20, 100, 60), [[0, 700], [540, 400], [1280, 720]])
    pygame.draw.polygon(screen, (50, 140, 90), [[150, 540], [540, 400], [200, 600]])
    
    pygame.draw.polygon(screen, (20, 100, 60), [[1440, 150], [1100, 350], [1280, 720]])
    pygame.draw.polygon(screen, (50, 140, 90), [[1050, 290], [1440, 150], [1100, 350]])
    
    pygame.draw.polygon(screen, (10, 60, 50), [[0, 500], [800, 720], [0, 720]])
    
    pygame.draw.polygon(screen, (10, 80, 40), [[0, 570], [430, 520], [610, 510], [820, 300], [1020, 290], [1280, 310], [1280, 720], [0, 720]])
    pygame.draw.polygon(screen, (60, 140, 100), [[820, 300], [850, 600], [430, 520]])


# Game functions
def process_input():
    """Handle user input events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        
        elif event.type == pygame.KEYDOWN:
            music_playing = pygame.mixer.music.get_busy()
            if event.key == pygame.K_p and music_playing == False:
                pygame.mixer.music.play(0)
                
    return True


def update(FPS):
    """Update game logic (e.g., movement, game state changes)."""
    music_playing = pygame.mixer.music.get_busy()
    if random.randint(0, 10000) == 0 and music_playing == False:
        pygame.mixer.music.play(0)


def draw():
    """Draw everything to the screen."""

    # pygame.draw.shape(screen, color, [position])
    draw_sky()
    draw_moon()
    draw_mountains()


def game_loop():
    """Main game loop."""
    clock = pygame.time.Clock()

    running = True
    while running:
        running = process_input()
        update(FPS)
        draw()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    game_loop()
