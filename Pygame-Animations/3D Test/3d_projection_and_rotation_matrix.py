# Imports
import math
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
CAPTION = "3D Rotation"
FPS = 60

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption(CAPTION)

center = [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH]
FOCUS_POINT = [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, -1280]
BLACK = (0, 0, 0)

star_coordinates = []
star_distance = 1080
cube_size = 360

orbital_dist = 720
sun_theta = 1
sun_phi = 1
sun_psi = 0
sun_normal = [0, 0, -1]

alpha = 0
beta = 0
gamma = -0.41

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

# Draw Functions

def draw_cube():
    # To draw a cube we need to do several things:
    # Find the 8 points defining the cube and turn them into 6 faces
    # Rotate those points in 3D Space
    # Check the surface normals and discard the faces with negative values
    # Project the remaining faces points onto the 2D Screen
    # Draw the polygons with lighting depending on the surface normals

    face = get_faces()
    color = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

    for n in range(6):
        side = face[n]
        normal = get_normal(side)

        projected = []
        for m in range(4):
            projected.append(project(side[m]))

        if find_dot_product(normal, [0, 0, -1]) > 0.05:
            pygame.draw.polygon(screen, get_color(normal, color[n]), projected)


def get_faces():
    # center = (x, y, z)
    # distance = (side_x, side_y, side_z)

    distance = cube_size # side length [x, y, z]

    minus = -distance / 2
    plus = distance / 2

    initial = [ [minus , minus , minus], # position[0]
                [plus , minus , minus],  # position[1]
                [minus , plus , minus],
                [plus , plus , minus],
                [minus , minus , plus],
                [plus , minus , plus],
                [minus , plus , plus],
                [plus , plus , plus] ]   # position[7]

    position = []
    for n in range( len(initial) ):
        point = initial[n]
        new_point = []
        
        for m in range(3):
            coord = point[m] + center[m]
            new_point.append(coord)
            
        position.append(new_point)

    for n in range( len(position) ):
        position[n] = three_dim_rotator(position[n], [alpha, beta, gamma])

    # defines the faces of the square
    # Needs to be ordered in a way that the normals of all the surfaces point out of the square
    surface_top = [ position[0], position[1], position[5], position[4] ]
    surface_bot = [ position[2], position[6], position[7], position[3] ]
    surface_nea = [ position[0], position[2], position[3], position[1] ]
    surface_far = [ position[4], position[5], position[7], position[6] ]
    surface_rig = [ position[1], position[3], position[7], position[5] ]
    surface_lef = [ position[0], position[4], position[6], position[2] ]

    faces = [surface_top, surface_bot, surface_far, surface_nea, surface_lef, surface_rig]
    
    return faces


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


def find_dot_product(vector1, vector2):
    # Find the dot product between the camera's normal vector and the given vector
    # Dot product = a1*b1 + a2*b2 + a3*b3
    
    dot_product = vector1[0] * vector2[0] + vector1[1] * vector2[1] + vector1[2] * vector2[2]
    return dot_product


def get_color(normal, color):
    # Take the dot product between the normal and some arbitrary light direction and scale the color accordingly

    lighting = find_dot_product(normal, sun_normal)
    
    if lighting <= 0.05:
        lighting = 0.05
        
        
    color = (color[0] * lighting, color[1] * lighting, color[2] * lighting)
    return color

    
def draw_stars(in_front):
    for n in range( len(star_coordinates) ):
        polar_coord = star_coordinates[n]
        
        cart_coord = convert_to_cartesian(star_distance, polar_coord[0], polar_coord[1])
        projected = project(cart_coord)

        temperature = polar_coord[3]

        red = -11 * (temperature - 3)**2 + 220
        green = -15 * (temperature - 4)**2 + 210
        blue = -7 * (temperature - 7)**2 + 225
        
        color = [red, green, blue]

        radius = polar_coord[2]

        if in_front == True:
            # Draw between the focus point and the center of the cube
            if cart_coord[2] >= FOCUS_POINT[2] and center[2] >= cart_coord[2]:
                pygame.draw.ellipse(screen, color, [projected[0] + radius, projected[1] + radius, 2 * radius, 2 * radius])
        else:
            # Draw beyond the center of the cube
            if cart_coord[2] > center[2]:
                pygame.draw.ellipse(screen, color, [projected[0] + radius, projected[1] + radius, 2 * radius, 2 * radius])
                            

def convert_to_cartesian(radius, theta, phi):
    x = radius * math.cos(theta) * math.cos(phi) + center[0]
    y = radius * math.sin(theta) * math.cos(phi) + center[1]
    z = radius * math.sin(phi) + center[2]

    cart_coord = [x, y, z]

    point = three_dim_rotator(cart_coord, [alpha, beta, gamma])
    return point


def generate_stars():
    global star_coordinates
    for _ in range(1000):
        new_star = create_new_star()
        star_coordinates.append(new_star)


def create_new_star():
    theta = 2 * math.pi * random.random()
    phi = 2 * math.pi * random.random()
    
    radius = random.randint(2, 82) ** (1 / 4)
    temperature = (1.42 + 1.22 * random.random()) ** (2)

    return [theta, phi, radius, temperature]


def draw_sun(in_front):
    global sun_normal, sun_psi, orbital_dist
    sun_psi -= 0.1 / FPS

    point_x = - math.sin(sun_theta) * math.cos(sun_psi) - math.cos(sun_theta) * math.sin(sun_phi) * math.sin(sun_psi)
    point_y = math.cos(sun_theta) * math.cos(sun_psi) - math.sin(sun_theta) * math.sin(sun_phi) * math.sin(sun_psi)
    point_z = math.cos(sun_phi) * math.sin(sun_psi)

    x = orbital_dist * point_x + center[0]
    y = orbital_dist * point_y + center[1]
    z = orbital_dist * point_z + center[2]

    rotated_sun = three_dim_rotator([x, y, z], [alpha, beta, gamma])
    projected_sun = project(rotated_sun)

    norm_x, norm_y, norm_z = rotated_sun[0] - center[0], rotated_sun[1] - center[1], rotated_sun[2] - center[2]

    magnitude = math.sqrt(norm_x**2 + norm_y**2 + norm_z**2)
    sun_normal = [norm_x / magnitude, norm_y / magnitude, norm_z / magnitude]
        
    radius = 10

    if center[2] > rotated_sun[2] and in_front == True:
        pygame.draw.ellipse(screen, (255, 255, 220), [projected_sun[0] - radius, projected_sun[1] - radius, 2 * radius, 2 * radius])
    elif rotated_sun[2] > center[2] and in_front == False:
        pygame.draw.ellipse(screen, (255, 255, 220), [projected_sun[0] - radius, projected_sun[1] - radius, 2 * radius, 2 * radius])

    
# Game functions
def process_input():
    global focus_distance, alpha, beta, gamma, star_coordinates, star_distance, cube_size
    global sun_theta, sun_phi, sun_psi
    
    """Handle user input events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                alpha = 0
                beta = 0
                gamma = 0

                sun_theta = math.pi/2
                sun_phi = 0
                
                cube_size = 520
                
            if event.key == pygame.K_m:
                star_coordinates = []
                generate_stars()

    pressed_keys = pygame.key.get_pressed()

    # Rotation Controls

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

    # Star Controls

    if pressed_keys[pygame.K_LSHIFT]:
        star_distance += 10
    elif pressed_keys[pygame.K_LCTRL]:
        star_distance -= 10

    # Sun Controls

    if pressed_keys[pygame.K_LEFT]:
        sun_phi += math.pi/3 / FPS
    elif pressed_keys[pygame.K_RIGHT]:
        sun_phi -= math.pi/3 / FPS

    if pressed_keys[pygame.K_UP]:
        sun_theta += math.pi/3 / FPS
    elif pressed_keys[pygame.K_DOWN]:
        sun_theta -= math.pi/3 / FPS

    if pressed_keys[pygame.K_SPACE]:
        sun_psi += math.pi/3 / FPS

    # Cube Controls

    if pressed_keys[pygame.K_o]:
        cube_size += 10
    elif pressed_keys[pygame.K_p]:
        cube_size -= 10
            
    return True


def update():
    """Update game logic (e.g., movement, game state changes)."""
    global beta
    beta += 1 / (FPS * 20)


def draw():
    screen.fill(BLACK)
    draw_stars(False)
    draw_sun(False)
    
    draw_cube()
    
    draw_sun(True)
    draw_stars(True)



def game_loop():
    """Main game loop."""
    clock = pygame.time.Clock()
    generate_stars()

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
