'''
3D Cube Refactored
'''

import math
import pygame
import random

# Set up display
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720
CAPTION = "3D Rotation"
FPS = 60

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption(CAPTION)

center = [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH]
FOCUS_POINT = [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, -1280]

alpha, beta, gamma = 0, 0, 0
std_rot = [alpha, beta, gamma]

star_distance = 360
star_theta_phi = []
star_initials = []
draw_star = []

cube_size = 100

sun_screen_pos = []
cube_screen_pos = []
star_screen_pos = []

sun_theta = 0

# Star Generating Functions
def generate_star_initials():
    global star_initials, draw_star
    
    for n in range(1000):
        star_initials.append(create_star())
        draw_star.append(False)


def change_star_distance():
    global star_initials

    for n in range(len(star_initials)):
        star_polar = star_theta_phi[n]
        star_carte = star_initials[n]
        
        radius, color = star_carte[3], star_carte[4]
        cartesian = convert_to_cartesian(star_distance, star_polar[0], star_polar[1])
        x, y, z = cartesian[0], cartesian[1], cartesian[2]

        star_initials[n] = [x, y, z, radius, color]

def create_star():
    global star_theta_phi
    theta = 2 * math.pi * random.random()
    phi = 2 * math.pi * random.random()

    star_theta_phi.append([theta, phi])
    
    radius = random.randint(2, 82) ** (1 / 4)
    temperature = 40 * (random.random() - (3/10)) ** 3 + 5

    cartesian = convert_to_cartesian(star_distance, theta, phi)
    x, y, z = cartesian[0], cartesian[1], cartesian[2]
    
    color = get_star_color(temperature)
    return [x, y, z, radius, color]


def convert_to_cartesian(radius, theta, phi):
    x = radius * math.cos(theta) * math.cos(phi) + center[0]
    y = radius * math.sin(theta) * math.cos(phi) + center[1]
    z = radius * math.sin(phi) + center[2]
    return [x, y, z]


def get_star_color(temperature):
    # Takes in a Temperature (in 1000K) and returns the approximate color of a Black Body of that Temperature
    if temperature < 7:
        red = 255
        green = -5 * math.e ** -(temperature - 7) + 245
        blue = -10 * math.e ** -(temperature - 7) + 265

    elif temperature == 7:
        red = 255
        green = 240
        blue = 255

    elif temperature > 7:
        red = 105 * math.e ** (-(temperature - 7) / 4) + 150
        green = 80 * math.e ** (-(temperature - 7) / 11) + 160
        blue = 255
        
    return [red, green, blue]


# Math functions
def project(point):
    t = - FOCUS_POINT[2] / (point[2] - FOCUS_POINT[2])
    x = FOCUS_POINT[0] + t * (point[0] - FOCUS_POINT[0])
    y = FOCUS_POINT[1] + t * (point[1] - FOCUS_POINT[1])
    projected_point = [x, y] 
    return projected_point


def three_dim_rotator(point, rotation):
    # This function takes in a point in 3D space
    # as well as a rotation about Alpha, Beta, and Gamma (Roll, Pitch, and Yaw)
    # and returns a new point with the rotation applied
    
    x = point[0] - center[0]
    y = point[1] - center[1]
    z = point[2] - center[2]

    theta = rotation[0]
    phi = rotation[1]
    psi = rotation[2]

    sinA = math.sin(alpha)
    cosA = math.cos(alpha)
    sinB = math.sin(beta)
    cosB = math.cos(beta)
    sinG = math.sin(gamma)
    cosG = math.cos(gamma)

    # 3D rotation matrix
    # [ cos(B)cos(G)  sin(A)sin(B)cos(G) - cos(A)sin(G)  cos(A)sin(B)cos(G) + sin(A)sin(G) ] [x]
    # [ cos(B)sin(G)  sin(A)sin(B)sin(G) + cos(A)cos(G)  cos(A)sin(B)sin(G) - sin(A)cos(G) ] [y]
    # [ -sin(B)       sin(A)cos(B)                       cos(A)cos(B)                      ] [z]

    new_x = x * (cosB * cosG)  +  y * (sinA * sinB * cosG - cosA * sinG)  +  z * (cosA * sinB * cosG + sinA * sinG) + center[0]
    new_y = x * (cosB * sinG)  +  y * (sinA * sinB * sinG + cosA * cosG)  +  z * (cosA * sinB * sinG - sinA * cosG) + center[1]
    new_z = x * (-sinB)        +  y * (sinA * cosB)                       +  z * (cosA * cosB)                      + center[2]

    new_point = [new_x, new_y, new_z]
    return new_point


def get_normal(points):
    point1, point2, point3 = points[1], points[2], points[3]
    
    x1, y1, z1 = point1[0], point1[1], point1[2]
    x2, y2, z2 = point2[0], point2[1], point2[2]
    x3, y3, z3 = point3[0], point3[1], point3[2]

    # Find the surface Normal of the points
    # Define 2 vectors based off the 3 given points
    vector1 = [ [x2 - x1], [y2 - y1], [z2 - z1] ]
    vector1 = [ [x3 - x1], [y3 - y1], [z3 - z1] ]

    # Find the cross product
    product_x = (y2 - y1) * (z3 - z1) - (z2 - z1) * (y3 - y1)
    product_y = (z2 - z1) * (x3 - x1) - (x2 - x1) * (z3 - z1)
    product_z = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

    unnormalized = [ product_x, product_y, product_z]
    magnitude = math.sqrt( product_x**2 + product_y**2 + product_z**2)

    if magnitude > 0:
        surface_normal = [ product_x / magnitude, product_y / magnitude, product_z / magnitude ]
    else:
        print("Cannot find surface normal on points that are co-linear.")
        surface_normal = [0,0,0]
    return surface_normal


# Update Functions

def find_sun_location():
    global sun_theta, sun_normal, sun_screen_pos
    
    sun_theta -= 0.1 / FPS
    orbital_dist = 300

    x = orbital_dist * math.cos(sun_theta) + center[0]
    y = center[1]
    z = orbital_dist * math.sin(sun_theta) + center[2]

    rotated_sun = three_dim_rotator([x, y, z], [alpha, beta, gamma])
    sun_screen_pos = project(rotated_sun)

    magnitude = math.sqrt(rotated_sun[0]**2 + rotated_sun[1]**2 + rotated_sun[2]**2)
    sun_normal = [-rotated_sun[0] / magnitude, -rotated_sun[1] / magnitude, -rotated_sun[2] / magnitude]


def find_star_locations():
    global star_screen_pos
    
    star_real_pos = []
    for n in range(len(star_initials)):
        star_screen_pos.append(n)
        rotated = three_dim_rotator(star_initials[n], std_rot)
        star_real_pos.append(rotated)
        star_screen_pos[n] = project(rotated)

        if rotated[2] > FOCUS_POINT[2]:
            draw_star[n] = True
        else:
            draw_star[n] = False


def find_cube_locations():
    # Get Cube Points
    # Rotate Points
    # Do Surface Wrapping
    pass


# Draw Functions

def draw_sun():
    radius = 10
    if (center[2] > rotated_sun[2] and in_front == True) or (rotated_sun[2] > center[2] and in_front == False):
        pygame.draw.ellipse(screen, (255, 255, 220), [sun_screen_pos[0] - radius, sun_screen_pos[1] - radius, 2 * radius, 2 * radius])


def draw_stars():
    for n in range(len(star_initials)):
        point = star_screen_pos[n]
        characteristics = star_initials[n]
        
        x, y = point[0], point[1]
        radius, color = characteristics[3], characteristics[4]

        if draw_star[n] == True:
            pygame.draw.ellipse(screen, color, [x - radius, y - radius, 2 * radius, 2 * radius])

def draw_cube():
    pass


# Game functions
def process_input():
    global alpha, beta, gamma
    global star_distance, star_initials
    
    """Handle user input events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                alpha = 0
                beta = 0
                gamma = 0
                cube_size = 100
                
            if event.key == pygame.K_m:
                star_initials = []
                star_screen_pos = []
                generate_star_initials()

    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[pygame.K_w]:
        alpha -= math.pi / FPS
    elif pressed_keys[pygame.K_s]:
        alpha += math.pi / FPS

    if pressed_keys[pygame.K_a]:
        beta += math.pi / FPS
    elif pressed_keys[pygame.K_d]:
        beta -= math.pi / FPS

    if pressed_keys[pygame.K_q]:
        gamma -= math.pi / FPS
    elif pressed_keys[pygame.K_e]:
        gamma += math.pi / FPS

    if pressed_keys[pygame.K_SPACE] or pressed_keys[pygame.K_BACKSPACE]:
        if pressed_keys[pygame.K_SPACE]:
            star_distance += 10
        elif pressed_keys[pygame.K_BACKSPACE]:
            star_distance -= 10

        change_star_distance()
        
    if pressed_keys[pygame.K_o]:
        cube_size += 10
    elif pressed_keys[pygame.K_p]:
        cube_size -= 10
            
    return True


def update():
    """Update game logic (e.g., movement, game state changes)."""
    find_sun_location()
    find_cube_locations()
    find_star_locations()
    
    global beta
    beta += 1 / (FPS * 20)


def draw():
    screen.fill((0, 0, 0))
    draw_stars()


def game_loop():
    """Main game loop."""
    clock = pygame.time.Clock()
    generate_star_initials()

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
