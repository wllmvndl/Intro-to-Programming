"""
gravity
"""

# Imports
import pygame
import math
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720
CAPTION = "Window Title"
FPS = 60

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption(CAPTION)

GRAVITY = 5
all_planets = []
remove_queue = []

offset_x = 0
offset_y = 0

new_planet_pos = []
new_planet_visible = False
mouse_pos = []

def initialize_planets():
    global all_planets
    
    all_planets = [Planet(5, (255, 0, 0), [200, 200], [50, -50]),
                   Planet(5, (0, 0, 255), [520, 520], [-50, 50])]
class Planet:
    def __init__(self, mass, color, position, velocity):
        self.mass = mass
        self.radius = 5 * math.cbrt(mass)
        self.color = color
        
        self.x = position[0]
        self.y = position[1]

        self.velo_x = velocity[0] / FPS
        self.velo_y = velocity[1] / FPS
        
        self.accl_x = 0
        self.accl_y = 0

    def find_acceleration(self):
        self.accl_x = 0
        self.accl_y = 0
        for n in range(len(all_planets)):
            other = all_planets[n]
            distance = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

            if distance == 0:
                pass
            
            elif distance < (self.radius + other.radius) / 2:
                self.merge(other)
        
            elif distance <= self.radius + other.radius:
                acceleration = other.mass / distance
                angle = math.atan2(other.y - self.y, other.x - self.x)

                self.accl_x -= acceleration * math.cos(angle)
                self.accl_y -= acceleration * math.sin(angle)
                
            else:
                acceleration = GRAVITY * other.mass / (distance ** 2)
                angle = math.atan2(other.y - self.y, other.x - self.x)
                
                self.accl_x += acceleration * math.cos(angle)
                self.accl_y += acceleration * math.sin(angle)

    def merge(self, other):
        global remove_queue
        
        if self not in remove_queue:
            total_mass = self.mass + other.mass

            self.x = (self.x * self.mass + other.x * other.mass) / total_mass
            self.y = (self.y * self.mass + other.y * other.mass) / total_mass

            self.velo_x = (self.velo_x * self.mass + other.velo_x * other.mass) / total_mass
            self.velo_x = (self.velo_y * self.mass + other.velo_y * other.mass) / total_mass

            self.color = ((self.color[0] * self.mass + other.color[0] * other.mass) / total_mass,
                          (self.color[1] * self.mass + other.color[1] * other.mass) / total_mass,
                          (self.color[2] * self.mass + other.color[1] * other.mass) / total_mass)

            self.mass = total_mass
            self.radius = 5 * math.cbrt(total_mass)
            other.mass = 0

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
    global all_planets
    global mouse_pos
    global new_planet_pos, new_planet_visible
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                initialize_planets()
            elif event.key == pygame.K_SPACE:
                for n in range(len(all_planets)):
                    all_planets[n].velo_x = all_planets[n].velo_x * 0.2
                    all_planets[n].velo_y = all_planets[n].velo_y * 0.2

        if event.type == pygame.MOUSEBUTTONDOWN:
            new_planet_pos = pygame.mouse.get_pos()
            new_planet_visible = True

        if event.type == pygame.MOUSEBUTTONUP:
            new_planet_visible = False
            mouse_pos = pygame.mouse.get_pos()
            
            angle = math.atan2(new_planet_pos[1] - mouse_pos[1], new_planet_pos[0] - mouse_pos[0])
            velocity = math.sqrt((new_planet_pos[0] - mouse_pos[0])**2 + (new_planet_pos[1] - mouse_pos[1])**2)
            velocity_vector = (velocity * math.cos(angle), velocity * math.sin(angle))
            all_planets.append(Planet(3, (255, 255, 255), new_planet_pos, velocity_vector))

        mouse_pressed = pygame.mouse.get_pressed()

        if mouse_pressed[0]:
            mouse_pos = pygame.mouse.get_pos()
            
    return True


def update():
    global all_planets, remove_queue
    for n in range(len(all_planets)):
        all_planets[n].find_acceleration()
    
    for m in range(len(all_planets)):
        all_planets[m].move()

    for o in range(len(all_planets)):
        all_planets[o]

    for p in range(len(remove_queue)):
        all_planets.remove(remove_queue[p])
    remove_queue = []


def draw():
    screen.fill((0, 0, 0))
    for n in range(len(all_planets)):
        all_planets[n].draw()

    if new_planet_visible:
        radius = 5
        pygame.draw.ellipse(screen, (200, 200, 255), [new_planet_pos[0] - radius + offset_x,
                                                      new_planet_pos[1] - radius + offset_y,
                                                      2 * radius, 2 * radius])
        
        pygame.draw.line(screen, (200, 200, 255), new_planet_pos, mouse_pos)


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
