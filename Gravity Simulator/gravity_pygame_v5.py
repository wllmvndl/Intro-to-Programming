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
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
CAPTION = "Window Title"
FPS = 60

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption(CAPTION)

GRAVITY = 1
all_planets = []
planet_count = 0
remove_queue = []
add_queue = []

offset_x = 0
offset_y = 0

new_planet_pos = []
new_planet_visible = False
mouse_pos = []

updating = True
drawing_vectors = False
explosions = False

new_planet_mass = 1

clack_snd = pygame.mixer.Sound('assets/sounds/clack.ogg')
sonar_snd = pygame.mixer.Sound('assets/sounds/sonar.ogg')
bloop_snd = pygame.mixer.Sound('assets/sounds/bloop.ogg')

def initialize_planets():
    global all_planets, planet_count
    
    all_planets = [Planet(5, (255, 0, 0), [200, 200], [50, -50]),
                   Planet(5, (0, 0, 255), [SCREEN_WIDTH - 200, SCREEN_HEIGHT - 200], [-50, 50]),
                   Planet(100, (255, 255, 0), [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2], [0, 0])]

    all_planets = [Planet(5, (255, 0, 0), [200, 200], [50, -50]),
                   Planet(5, (0, 0, 255), [SCREEN_WIDTH - 200, SCREEN_HEIGHT - 200], [-50, 50])]
    
    planet_count = len(all_planets)


class Planet:
    def __init__(self, mass, color, position, velocity):
        self.mass = mass
        self.radius = 2 * math.cbrt(mass)
        self.color = color
        
        self.x = position[0]
        self.y = position[1]

        self.velo_x = velocity[0] / FPS
        self.velo_y = velocity[1] / FPS
        
        self.accl_x = 0
        self.accl_y = 0

        self.split_cooldown = 10

        if self.radius > 0:
            self.surface_gravity = GRAVITY * self.mass / (self.radius)**2
        else:
            self.surface_gravity = 0

    def find_acceleration(self):
        if self in remove_queue:
            return

        if self.mass == 0 or self.radius == 0:
            return
            
        self.accl_x = 0
        self.accl_y = 0
        
        for n in range(planet_count):
            other = all_planets[n]
            distance = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
            angle = math.atan2(other.y - self.y, other.x - self.x)

            if other.mass > self.mass and distance - self.radius != 0:
                high_tide_gravity = 1.5 * GRAVITY * other.mass / (distance - self.radius)**2
            else:
                high_tide_gravity = 0

            if distance == 0 or other in remove_queue:
                pass

            if distance < (self.radius + other.radius) / 3 and other.mass > 2:
                other.explode()

            elif distance < 3 * (self.radius + other.radius) / 4:
                self.merge(other, angle)

                '''elif (self.radius + other.radius) / 2 < distance < self.radius + other.radius:
                    self.bounce(other, angle, distance)'''

            else:
                self.attrack(other, distance, angle)
                    
            if distance > self.radius + other.radius and self.surface_gravity < high_tide_gravity:
                if self.mass > 1:
                    self.split(other, distance, angle)

            if explosions == True and self.mass > 100 and random.randint(0, 1000) == 0:
                self.explode()
                    
    def attrack(self, other, distance, angle):
        acceleration = GRAVITY * other.mass / (distance ** 2)                
        self.accl_x += acceleration * math.cos(angle)
        self.accl_y += acceleration * math.sin(angle)

    def merge(self, other, angle):
        global all_queue, remove_queue
        
        if self not in remove_queue:
            clack_snd.play()
            bloop_snd.play()
            
            total_mass = self.mass + other.mass

            average_velo_x = (self.velo_x * self.mass + other.velo_x * other.mass) / total_mass
            average_velo_y = (self.velo_y * self.mass + other.velo_y * other.mass) / total_mass

            position = [(self.x * self.mass + other.x * other.mass) / total_mass + average_velo_x,
                        (self.y * self.mass + other.y * other.mass) / total_mass + average_velo_y]

            velocity = [FPS * average_velo_x,
                        FPS * average_velo_y]

            color = ((self.color[0] * self.mass + other.color[0] * other.mass) / total_mass,
                     (self.color[1] * self.mass + other.color[1] * other.mass) / total_mass,
                    ( self.color[2] * self.mass + other.color[2] * other.mass) / total_mass)

            mass = total_mass
            
            self.mass = 0
            self.radius = 0

            add_queue.append(Planet(mass, color, position, velocity))
            remove_queue.append(self)
            remove_queue.append(other)

    def bounce(self, other, distance, angle):
        if self in remove_queue:
            return

        if self.mass == 0 or distance == 0:
            return

        sonar_snd.play()
        '''
        acceleration = other.mass / (distance - other.radius)

        self.accl_x -= acceleration * math.cos(angle)
        self.accl_y -= acceleration * math.sin(angle)
        '''
        

    def split(self, other, distance, angle):
        global all_queue, remove_queue, updating

        if self.split_cooldown != 0:
            self.attrack(other, distance, angle)
            return
        
        bloop_snd.play()

        mass = self.mass / 2
        position = [self.x + self.radius * math.cos(angle) + 2 * self.velo_x,
                    self.y + self.radius * math.sin(angle) + 2 * self.velo_y]
        velocity = [self.velo_x,
                    self.velo_y]
        add_queue.append(Planet(mass, self.color, position, velocity))

        self.mass = self.mass / 2
        self.radius = 2 * math.cbrt(self.mass)
        self.x = self.x - self.radius * math.cos(angle) + self.velo_x
        self.y = self.y - self.radius * math.sin(angle) + self.velo_y

        self.split_cooldown += 20

    def explode(self):
        if self.mass < 10:
            upper_bound = self.mass
        else:
            upper_bound = 10

        planets = random.randint(1, upper_bound)
        sonar_snd.play()

        for n in range(planets):
            delta_angle = 360 / planets

            position = [self.x + 2 * self.radius * math.cos(n * delta_angle), 
                        self.y + 2 * self.radius * math.sin(n * delta_angle)]
            
            velocity = [self.velo_x + 5 * FPS * self.surface_gravity * math.cos(n * delta_angle),
                        self.velo_y + 5 * FPS * self.surface_gravity * math.sin(n * delta_angle)]

            new_planet = Planet(self.mass / planets, self.color, position, velocity)
            add_queue.append(new_planet)
            remove_queue.append(self)

    def move(self):
        if self.split_cooldown > 0:
            self.split_cooldown -= 1
        
        self.velo_x += self.accl_x
        self.velo_y += self.accl_y

        self.x += self.velo_x
        self.y += self.velo_y
        
        if self.x < 0 - offset_x:
            self.x = 0
            self.velo_x = -self.velo_x
            bloop_snd.play()

        if self.x > SCREEN_WIDTH - offset_x:
            self.x = SCREEN_WIDTH
            self.velo_x = -self.velo_x
            bloop_snd.play()

        if self.y < 0 - offset_y:
            self.y = 0
            self.velo_y = -self.velo_y
            bloop_snd.play()
            
        if self.y > SCREEN_HEIGHT - offset_y:
            self.y = SCREEN_HEIGHT
            self.velo_y = -self.velo_y
            bloop_snd.play()
        

    def draw_planet(self):
        pygame.draw.ellipse(screen, self.color, [self.x - self.radius + offset_x,
                                                 self.y - self.radius + offset_y,
                                                 2 * self.radius, 2 * self.radius])
        
    def draw_vector(self):
        pygame.draw.line(screen, (255, 255, 255), [self.x, self.y],
                         [self.x + self.velo_x * 10, self.y + self.velo_y * 10])
        

def update_accelerations():
    for n in range(planet_count):
        all_planets[n].find_acceleration()

def move_planets():
    for n in range(planet_count):
        all_planets[n].move()

def remove_planets():
    global all_planets, remove_queue
    for n in range(len(remove_queue)):
        if remove_queue[n] in all_planets:
            all_planets.remove(remove_queue[n])
    remove_queue = []

def add_planets():
    global all_planets, add_queue
    for n in range(len(add_queue)):
        all_planets.append(add_queue[n])
    add_queue = []

def draw_planets():
    for n in range(planet_count):
        all_planets[n].draw_planet()
        if drawing_vectors:
            all_planets[n].draw_vector()

def draw_ghost():
    if new_planet_visible:
        radius =  2 * math.cbrt(new_planet_mass) - 1
        pygame.draw.ellipse(screen, (200, 200, 255), [new_planet_pos[0] - radius + offset_x,
                                                      new_planet_pos[1] - radius + offset_y,
                                                      2 * radius, 2 * radius])
        
        pygame.draw.line(screen, (200, 200, 255), new_planet_pos, mouse_pos)

def find_center_of_mass():
    global offset_x, offset_y
    total_mass = 0
    for n in range(planet_count):
        total_mass += all_planets[n].mass

    offset_x = 0
    for m in range(planet_count):
        offset_x += all_planets[n].x * all_planets[n].mass / total_mass

    offset_y = 0
    for o in range(planet_count):
        offset_y += all_planets[n].y * all_planets[n].mass / total_mass

    offset_x -= SCREEN_WIDTH
    offset_y -= SCREEN_HEIGHT

    print(offset_x)
    print(offset_y)
    print()

# Game functions
def process_input():
    global all_planets
    global updating, drawing_vectors, explosions
    global mouse_pos, new_planet_pos, new_planet_visible, new_planet_mass
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
            
            if event.key == pygame.K_r:
                initialize_planets()
                
            elif event.key == pygame.K_LCTRL:
                for n in range(planet_count):
                    all_planets[n].velo_x = all_planets[n].velo_x * 0.2
                    all_planets[n].velo_y = all_planets[n].velo_y * 0.2

            elif event.key == pygame.K_SPACE:
                updating = not updating

            elif event.key == pygame.K_v:
                drawing_vectors = not drawing_vectors

            elif event.key == pygame.K_x:
                explosions = not explosions

            elif event.key == pygame.K_9:
                new_planet_mass = 100
            
            elif event.key == pygame.K_0:
                new_planet_mass = 1000

            num_keys = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5]

            if event.key in num_keys:
                new_planet_mass = num_keys.index(event.key) + 1

        if event.type == pygame.MOUSEBUTTONDOWN:
            new_planet_pos = pygame.mouse.get_pos()
            new_planet_visible = True

        if event.type == pygame.MOUSEBUTTONUP:
            new_planet_visible = False
            mouse_pos = pygame.mouse.get_pos()
            
            angle = math.atan2(new_planet_pos[1] - mouse_pos[1], new_planet_pos[0] - mouse_pos[0])
            velocity = math.sqrt((new_planet_pos[0] - mouse_pos[0])**2 + (new_planet_pos[1] - mouse_pos[1])**2)
            velocity_vector = (velocity * math.cos(angle), velocity * math.sin(angle))
            all_planets.append(Planet(new_planet_mass, (255, 255, 255), new_planet_pos, velocity_vector))

        mouse_pressed = pygame.mouse.get_pressed()

        if mouse_pressed[0]:
            mouse_pos = pygame.mouse.get_pos()
            
    return True


def update():
    global planet_count
    if updating:
        update_accelerations()
        move_planets()
        remove_planets()
        add_planets()
        planet_count = len(all_planets)
        #find_center_of_mass()


def draw():
    screen.fill((0, 0, 0))
    draw_planets()
    draw_ghost()


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
