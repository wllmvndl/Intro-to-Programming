"""
gravity
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

GRAVITY = 0.1
all_planets = []
remove_queue = []

offset_x = 0
offset_y = 0

def initialize_planets():
    global all_planets
    all_planets = [Planet(5, (255, 0, 0), [540, 540], [10, 0]),
                   Planet(5, (0, 255, 0), [100, 200], [20, 0]),
                   Planet(5, (0, 0, 255), [620, 100], [0, 0]) ]

class Planet:
    def __init__(self, mass, color, position, velocity):
        self.mass = mass
        self.radius = 5 * math.cbrt(mass)
        self.color = color
        
        self.x = position[0]
        self.y = position[1]

        self.velo_x = velocity[0] * math.cos(velocity[1]) / FPS
        self.velo_y = velocity[0] * math.sin(velocity[1]) / FPS
        
        self.accl_x = 0
        self.accl_y = 0

    def sum_forces(self):
        self.accl_x = 0
        self.accl_y = 0
        
        for n in range(len(all_planets)):
            other = all_planets[n]
            if self != other:
                self.add_acceleration(other)

    def add_acceleration(self, other):
        distance = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

        if distance < self.radius + other.radius:
            self.merge(other)
        
        angle = math.atan2(other.y - self.y, other.x - self.x)
        force = GRAVITY * other.mass * self.mass / distance
        acceleration = force / self.mass

        self.accl_x = acceleration * math.cos(angle)
        self.accl_y = acceleration * math.sin(angle)

    def merge(self, other):
        global all_planets, remove_queue
        if self not in remove_queue:
            total_mass = self.mass + other.mass
            self.velo_x = (self.velo_x * self.mass + other.velo_x * other.mass) / total_mass
            self.velo_y = (self.velo_y * self.mass + other.velo_y * other.mass) / total_mass
            self.mass = total_mass
            self.radius = 5 * math.cbrt(total_mass)

            remove_queue.append(other)

    def move(self):
        self.velo_x += self.accl_x
        self.velo_y += self.accl_y

        self.x += self.velo_x
        self.y += self.velo_y

        if self.x < 0:
            self.velo_x = -self.velo_x
        elif self.x > SCREEN_WIDTH:
            self.velo_x = -self.velo_x

        if self.y < 0:
            self.velo_y = -self.velo_y
        elif self.y > SCREEN_HEIGHT:
            self.velo_y = -self.velo_y

    def draw(self):
        pygame.draw.ellipse(screen, self.color, [self.x - self.radius + offset_x,
                                                 self.y - self.radius + offset_y,
                                                 2 * self.radius, 2 * self.radius])
        
        pygame.draw.line(screen, (255, 255, 255), [self.x, self.y],
                         [self.x + self.velo_x * 10, self.y + self.velo_y * 10])

# Game functions
def process_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                initialize_planets()
    return True


def update():
    global all_planets, remove_queue
    for n in range(len(all_planets)):
        all_planets[n].sum_forces()

    for m in range(len(all_planets)):
        all_planets[m].move()

    for o in range(len(remove_queue)):
        all_planets.remove(remove_queue[o])

    remove_queue = []


def draw():
    screen.fill((0, 0, 0))
    for n in range(len(all_planets)):
        all_planets[n].draw()


def game_loop():
    clock = pygame.time.Clock()
    
    initialize_planets()

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
