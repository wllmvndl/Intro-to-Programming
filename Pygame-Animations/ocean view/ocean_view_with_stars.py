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
import random
import sys

# Initialize Pygame
pygame.init()

# Set up display
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
CAPTION = "My Awesome Picture"
FPS = 60

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption(CAPTION)

# Fonts
FONT_SM = pygame.font.Font(None, 48)
FONT_MD = pygame.font.Font(None, 64)
FONT_LG = pygame.font.Font(None, 96)

center_x, center_y = 1080, 200
star_count = 10000
star_coordinates = []

cloud_amount = 0
cloud_coordinates = []

def generate_stars():
    global star_coordinates
    for _ in range(star_count):
        new_star = generate_new_star()
        star_coordinates.append(new_star)
        

def generate_new_star():
    x = random.randint(0, SCREEN_WIDTH * 2)
    y = random.randint(-SCREEN_WIDTH, SCREEN_WIDTH)
    radius = math.sqrt( random.randint(2, 25) ) / 2
    
    theta = math.atan2(y - center_y, x - center_x)
    distance = math.sqrt( (x - center_x)**2 + (y - center_y)**2 )

    temperature = math.sqrt(random.randint(2, 50))

    red = -10 * (temperature - 3)**2 + 220
    green = -15 * (temperature - 4)**2 + 210
    blue = -11 * (temperature - 6)**2 + 240
    
    color = (red, green, blue)
    new_star = [theta, distance, radius, color]
    return new_star


def generate_clouds():
    global cloud_coordinates
    for _ in range(cloud_amount):
        new_cloud = generate_new_cloud()
        cloud_coordinates.append(new_cloud)


def generate_new_cloud():
    x = random.randint(-100, SCREEN_WIDTH)
    y = random.randint(-100, 300)
    cloud_type = random.randint(1, 3)

    cloud = [x, y, cloud_type]
    return cloud

# Draw functions
def draw_sky():
    color_sky = (10, 30, 60)
    color_upper_atm = (20, 60, 140)
    color_middle_atm = (30, 100, 180)
    color_lower_atm = (80, 150, 200)
    horizon_atm = (160, 240, 255)
    
    screen.fill(horizon_atm)
    pygame.draw.rect(screen, color_lower_atm, [0, 0, 1280, 355])
    pygame.draw.rect(screen, color_middle_atm, [0, 0, 1280, 340])
    pygame.draw.rect(screen, color_upper_atm, [0, 0, 1280, 300])
    pygame.draw.rect(screen, color_sky, [0, 0, 1280, 200])


def draw_stars(time):
    index = 0
    for _ in range(star_count):
        star = star_coordinates[index]
        theta = star[0]
        distance = star[1]
        
        radius = star[2]
        if random.randint(0, 30) == 0:
            radius -= 1
            
        color = star[3]
        rotation_speed = 10000
        pygame.draw.ellipse(screen, color, [distance * math.cos(theta - time / rotation_speed) - radius + center_x,
                                            distance * math.sin(theta - time / rotation_speed) - radius + center_y,
                                            radius * 2, radius * 2])
        index += 1


def draw_clouds():
    global cloud_coordinates
    
    index = 0
    for _ in range(cloud_amount):
        cloud = cloud_coordinates[index]
        x = cloud[0]
        y = cloud[1]
        cloud_type = cloud[2]

        width = cloud_type * 50
        height = cloud_type * 10

        cloud_speed = 100
        
        pygame.draw.rect(screen, (255, 255, 255), [x, y, width, height])
        
        index += 1
        x -= 10 / y


def draw_ocean():
    ocean_horizon = (10, 35, 60)
    ocean_middle = (0, 20, 40)
    ocean_deep = (0, 10, 20)

    pygame.draw.rect(screen, ocean_horizon, [0, 360, 1280, 360])
    pygame.draw.rect(screen, ocean_middle, [0, 410, 1280, 330])
    pygame.draw.rect(screen, ocean_deep, [0, 500, 1280, 220])


def draw_ground():
    ground_atm = (25, 80, 60)
    ground_1 = (20, 50, 40)
    ground_2 = (10, 60, 35)
    ground_3 = (5, 45, 30)
    ground_4 = ((15, 75, 50))

    pygame.draw.polygon(screen, ground_atm, [ [840, 360], [960, 350], [990, 355], [1060, 345], [1160, 355], [1280, 350], [1280,360] ])

    draw_clouds()
    
    pygame.draw.polygon(screen, ground_2, [ [830, 500], [1040, 460], [1060, 450], [1150, 410], [1130, 400], [1050, 380], [1000, 370],
                                            [960, 370], [950, 370], [1010, 360], [1140, 350], [1180, 345], [1280, 360], [1280, 600], [720, 600] ])
    pygame.draw.polygon(screen, ground_3, [ [1000, 390], [1140, 365], [1280, 360], [1280, 375]] )
    pygame.draw.polygon(screen, ground_atm, [ [1000, 390],  [1140, 365], [1030, 380] ])
    pygame.draw.polygon(screen, ground_4, [ [920, 410], [1060, 395], [1230, 370], [1280, 340], [1280, 400], [1150, 415] ])
    pygame.draw.polygon(screen, ground_2, [ [0, 520], [200, 540], [0, 570] ])
    pygame.draw.polygon(screen, ground_3, [ [0, 540], [100, 545], [250, 600], [250, 720], [0, 720] ])
    pygame.draw.polygon(screen, ground_1, [ [200, 600], [280, 590], [640, 580], [710, 530], [1020, 480], [1280, 470], [1280, 720], [200, 720] ])

    
# Game functions
def process_input():
    global star_coordinates, cloud_coordinates
    
    """Handle user input events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                star_coordinates = []
                generate_stars()
                cloud_coordinates = []
                generate_clouds()
                
    return True


def update():
    """Update game logic (e.g., movement, game state changes)."""


def draw(time):
    """Draw everything to the screen."""
    draw_sky()
    draw_stars(time)
    draw_ocean()
    draw_ground()


def game_loop():
    """Main game loop."""
    clock = pygame.time.Clock()
    generate_stars()
    generate_clouds()
    time = 0
    
    running = True
    while running:
        running = process_input()
        update()
        draw(time)

        time = time + 1

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    game_loop()
