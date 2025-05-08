"""
Pygame gravity simulator
"""

# Imports
import pygame
import math
import random
import sys

# Initialize Pygame
pygame.init()

# Set up display
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720
CAPTION = "Orbital Simulation"
FPS = 60

zoom = 0.5
GRAVITY = 1

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption(CAPTION)

offset_x, offset_y = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2

colors = [ (255, 0, 0), (0, 255, 0,), (0, 0, 255),
           (255, 255, 0), (255, 0, 255), (0, 255, 255) ]

all_planets = []

# Classes

class Planet:

    def __init__(self, n, x, y):
        self.mass = rand(1, 5)
        self.color = colors[n]
        self.radius = 15 * math.cbrt(self.mass)
        self.accl_x = 0
        self.accl_y = 0
        self.velo_x = rand(-50, 50) / 60
        self.velo_y = rand(-50, 50) / 60
        self.x = x
        self.y = y

    def move(self):
        self.find_sum_of_forces()
        
        self.velo_x += self.accl_x
        self.x += self.velo_x

        self.velo_y += self.accl_y
        self.y += self.velo_y

    def find_sum_of_forces(self):
        if self.mass != 0:
            for n in range(len(all_planets)):
                other = all_planets[n]
                if self != other and other.mass != 0:
                    angle = math.atan2(self.y - other.y, self.x - other.x)
                    distance = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

                    if distance < self.radius + other.radius and other.mass != 0:
                        self.merge(other)
                    
                    self.total_force = - GRAVITY * (self.mass * other.mass) / distance
                    
                    self.accl_x = self.total_force * math.cos(angle) / self.mass
                    self.accl_y = self.total_force * math.sin(angle) / self.mass

    def merge(self, other):
        if self.mass < other.mass:
            return
        else:
            self.color = ((self.mass * self.color[0] + other.mass * other.color[0]) / (self.mass + other.mass),
                          (self.mass * self.color[1] + other.mass * other.color[1]) / (self.mass + other.mass),
                          (self.mass * self.color[2] + other.mass * other.color[2]) / (self.mass + other.mass) )
            
            self.radius = 15 * math.cbrt(self.mass + other.mass)
            self.accl_x = (self.mass * self.accl_x + other.mass * other.accl_x) / (self.mass + other.mass)
            self.accl_y = (self.mass * self.accl_y + other.mass * other.accl_y) / (self.mass + other.mass)
            self.velo_x = (self.mass * self.velo_x + other.mass * other.velo_x) / (self.mass + other.mass)
            self.velo_y = (self.mass * self.velo_y + other.mass * other.velo_y) / (self.mass + other.mass)

            self.mass = (self.mass + other.mass)
            other.mass = 0

    def draw(self):
        if self.mass != 0:
            pygame.draw.ellipse(screen, self.color, [zoom * (self.x - self.radius) + offset_x,
                                                     zoom * (self.y - self.radius) + offset_y,
                                                     zoom * 2 * self.radius, zoom * 2 * self.radius])
            '''
            pygame.draw.line(screen, (255, 255, 255), [zoom * self.x + offset_x, zoom * self.y + offset_y],
                                                      [zoom * self.x + 50 * self.velo_x + offset_x,
                                                       zoom * self.y + 50 * self.velo_y + offset_y]) '''
                

def rand(low, high):
    return random.randint(low, high)


# Game functions
def process_input():
    global zoom, offset_x, offset_y
    global all_planets
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.MOUSEWHEEL:
            zoom += 0.1 * event.y
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pressed = pygame.mouse.get_pressed()

            if mouse_pressed[0]:
                mouse_pos = pygame.mouse.get_pos()
                all_planets.append(Planet(rand(0, 5), mouse_pos[0] + offset_x, mouse_pos[1] + offset_y))
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                zoom = 0.5
                offset_x = SCREEN_WIDTH / 2
                offset_y = SCREEN_HEIGHT / 2
                for n in range(len(all_planets)):
                    x, y = rand(-360, 360), rand(-360, 360)
                    all_planets[n].__init__(n % len(colors) - 1, x, y)

    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[pygame.K_w]:
        offset_y += 10
    elif pressed_keys[pygame.K_s]:
        offset_y -= 10

    if pressed_keys[pygame.K_a]:
        offset_x += 10
    elif pressed_keys[pygame.K_d]:
        offset_x -= 10
        
    return True


def update():
    for n in range(len(all_planets)):
        all_planets[n].move()


def draw():
    screen.fill((0, 0, 0))
    for n in range(len(all_planets)):
        all_planets[n].draw()


def game_loop():
    clock = pygame.time.Clock()
    global planet_1, planet_2, planet_3
    global all_planets

    for n in range(3):
        n = rand(0, len(colors) - 1)
        x, y = rand(-360, 360), rand(-360, 360)
        all_planets.append(Planet(n, x, y))


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
