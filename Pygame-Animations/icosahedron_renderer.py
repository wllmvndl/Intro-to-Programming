'''
3D program that can draw a concave shape
'''

# Imports
import math
import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up display
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720
CAPTION = "3D Concave Object"
FPS = 60

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption(CAPTION)

center = [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH]
FOCUS_POINT = [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, -1280]
BLACK = (0, 0, 0)

time = 0

alpha = math.pi / 2
beta = 0
gamma = math.pi / 12

alpha_accl = 0
beta_accl = -0.016
gamma_accl = 0

# Platonic solids
def get_point_cube(index): #LOL
    x = [1, 1, 1, 1, -1, -1, -1, -1] 
    y = [1, 1, -1, -1, 1, 1, -1, -1]
    z = [1, -1, 1, -1, 1, -1, 1, -1]
    point = [x[index], y[index], z[index]]
    return point


def get_point_icosahedron(index): #guh
    x = [0, 0, -0.8944, 0.8944, 0.7236, 0.7236, -0.7236, -0.7236, -0.2764, -0.2764, 0.2764, 0.2764]
    y = [0, 0, 0, 0, -0.5257, 0.5257, -0.5257, 0.5257, -0.8507, 0.8507, -0.8507, 0.8507]
    z = [-1, 1, -0.4472, 0.4472, -0.4472, -0.4472, 0.4472, 0.4472, -0.4472, -0.4472, 0.4472, 0.4472]
    point = [x[index], y[index], z[index]]
    return point


def get_point_dodecahedron(index): #not as funny
    x = []
    y = []
    z = []
    point = [x[index], y[index], z[index]]
    return point


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
    # Finds the normal vector of a 3 non-colinear points
    # Can take in any number of coplanar points, but only the first 3 are used, no detection if other points are on the surface
    point1, point2, point3 = points[0], points[1], points[2]
    
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
    sun_normal = [-math.sqrt(3)/3, -math.sqrt(3)/3, -math.sqrt(3)/3]
    lighting = find_dot_product(normal, sun_normal)
    
    if lighting <= 0.05:
        lighting = 0.05
        
    color = (color[0] * lighting, color[1] * lighting, color[2] * lighting)
    return color


def convert_to_cartesian(radius, theta, phi):
    # Takes in 3D polar coordinates and converts them to cartesian
    x = radius * math.cos(theta) * math.cos(phi) + center[0]
    y = radius * math.sin(theta) * math.cos(phi) + center[1]
    z = radius * math.sin(phi) + center[2]

    cart_coord = [x, y, z]

    point = three_dim_rotator(cart_coord, [alpha, beta, gamma])
    return point


# Draw Functions

def draw_concave(object_num, convex_num):
    # A concave shape (made up of polygons) can be desrcibed as multiple convex objects joined together
    # The order of being drawn will depend on which z value is lowest, as lower z values are closer to the camera plane
    convex_centers = [] 
    for n in range(convex_num):
        points = get_points(object_num, n)
        n_center = get_midpoint(points)
        convex_centers.append(n_center)


def draw_convex():
    # Draw a given convex shape given the specified object number and which index it is in the list
    pass



def get_midpoint(point_list):
    # Finds the midpoint of a given list of values
    x = 0
    y = 0
    z = 0
    
    for n in range( len(point_list) ):
        point = point_list[n]

        x = x + point[0]
        y = y + point[1]
        z = z + point[2]

    midpoint = [x, y ,z]
    return midpoint
        

def draw_point(radius, point, color):
    x = point[0] * radius + center[0]
    y = point[1] * radius + center[1]
    z = point[2] * radius + center[2]
    
    rotated = three_dim_rotator([x, y, z], [alpha, beta, gamma])
    projected = project(rotated)

    x = projected[0]
    y = projected[1]
    z = rotated[2]
    
    radius = 5000 / z

    if z > 0:
        pygame.draw.ellipse(screen, color, [x - radius, y - radius, 2 * radius, 2 * radius])



def draw_face(radius, color, point_list):
    rotated_points = []
    projected_points = []
    for n in range( len(point_list) ):
        point = point_list[n]

        x = point[0] * radius + center[0]
        y = point[1] * radius + center[1]
        z = point[2] * radius + center[2]
        
        rotated = three_dim_rotator([x, y, z], [alpha, beta, gamma])
        rotated_points.append(rotated)
        projected = project(rotated)
        projected_points.append(projected)

    normal = get_normal(rotated_points)
    
    if find_dot_product(normal, [0, 0, -1]) > 0.15:
        pygame.draw.polygon(screen, get_color(normal, color), projected_points)


def draw_icosahedron(radius):
    icosahedron_surface_wrapped = [ [0, 2, 9], [0, 4, 8], [0, 5, 4], [0, 8, 2], [0, 9, 5],
                                    [1, 3, 11], [1, 6, 10], [1, 7, 6], [1, 10, 3], [1, 11, 7],
                                    [2, 6, 7], [2, 7, 9], [2, 8, 6],
                                    [3, 10, 4], [3, 4, 5], [3, 5, 11],
                                    [4, 10, 8], [5, 9, 11], [6, 8, 10], [7, 11, 9] ]

    for n in range( len(icosahedron_surface_wrapped) ):
        wrap = icosahedron_surface_wrapped[n]
        
        draw_face(radius,
                  (255,
                   0,
                   0),
                  [get_point_icosahedron(wrap[0]),
                   get_point_icosahedron(wrap[1]),
                   get_point_icosahedron(wrap[2])])
        

# Game functions
def process_input():
    global alpha, beta, gamma
    global alpha_accl, beta_accl, gamma_accl
    
    """Handle user input events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                alpha = math.pi / 2
                beta = 0
                gamma = 0

                alpha_accl = 0
                beta_accl = 0
                gamma_accl = 0

    pressed_keys = pygame.key.get_pressed()

    # Rotation Controls

    max_accl = 0.1
    acceleration = 0.002

    if max_accl > alpha_accl and pressed_keys[pygame.K_s]:
        alpha_accl += acceleration
    elif alpha_accl > -max_accl and pressed_keys[pygame.K_w]:
        alpha_accl -= acceleration

    if max_accl > beta_accl and pressed_keys[pygame.K_a]:
        beta_accl += acceleration
    elif beta_accl > -max_accl and pressed_keys[pygame.K_d]:
        beta_accl -= acceleration

    if max_accl > gamma_accl and pressed_keys[pygame.K_e]:
        gamma_accl += acceleration
    elif gamma_accl > -max_accl and pressed_keys[pygame.K_q]:
        gamma_accl -= acceleration

    if pressed_keys[pygame.K_SPACE]:
        if alpha_accl > 0:
            alpha_accl -= acceleration
        elif alpha_accl < 0:
            alpha_accl += acceleration

        if beta_accl > 0:
            beta_accl -= acceleration
        elif beta_accl < 0:
            beta_accl += acceleration

        if gamma_accl > 0:
            gamma_accl -= acceleration
        elif gamma_accl < 0:
            gamma_accl += acceleration
            
    return True


def update():
    """Update game logic (e.g., movement, game state changes)."""
    global time
    global alpha, beta, gamma
    global alpha_accl, beta_accl, gamma_accl

    time += 1
    
    alpha += alpha_accl
    beta += beta_accl
    gamma += gamma_accl


def draw():
    screen.fill(BLACK)
    '''
    for n in range(12):
        draw_point(360, get_point_icosahedron(n), (255, 255, 255))
    '''
    draw_icosahedron(360)
    

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
