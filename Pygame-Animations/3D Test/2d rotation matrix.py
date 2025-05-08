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

# Initialize Pygame
pygame.init()

# Set up display
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CAPTION = "2D Rotation"
FPS = 60

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption(CAPTION)

# Colors
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)

theta = 0

def draw_square(speed):
    global theta
    
    points = [ [100, 100], [100, -100], [-100, -100], [-100, 100] ]
    new_points = []
    index = 0
    for _ in range( len(points)):
        new_points.append( rotate(points[index]) )
        index += 1
    
    pygame.draw.polygon(screen, CYAN, new_points, 4)
    theta += speed


def rotate(point):
    # 2D rotation matrix
    # [cosΘ  -sinΘ] [x]  [xcosΘ - ysinΘ]
    # [sinΘ  cosΘ ] [y]  [xsinΘ + ycosΘ]

    x = point[0] * math.cos(theta) - point[1] * math.sin(theta) + SCREEN_WIDTH / 2
    y = point[0] * math.sin(theta) + point[1] * math.cos(theta) + SCREEN_HEIGHT / 2

    return [x, y]

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
    screen.fill(BLACK)
    draw_square(math.pi / 60)
    draw_square(math.pi / 120)


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


if __name__ == "__main__":
    game_loop()
