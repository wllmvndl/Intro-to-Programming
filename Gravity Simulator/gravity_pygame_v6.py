import pygame
import math

import objects
import settings

class Game:
    def __init__(self):
        # Initialize Pygame
        pygame.mixer.pre_init()
        pygame.init()

        # Make window
        self.screen = pygame.display.set_mode([settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT])
        pygame.display.set_caption(settings.CAPTION)
        self.clock = pygame.time.Clock()
        self.running = True

        # object lists
        self.all_planets = []
        self.planet_count = 0
    
        # Game Variables
        self.gravity = 1

        self.updating = True
        self.showing_vectors = False
        self.drawing_ghost = False

        self.mouse_pos = [0, 0]
        self.new_planet_pos = [0, 0]
        self.new_planet_mass = 1

        self.remove_queue = []
        self.add_queue = 0

        # Set up game
        self.load_assets()
        self.new_game()

    def load_assets(self):
        self.clack_snd = settings.CLACK_SND
        self.sonar_snd = settings.SONAR_SND
        self.bloop_snd = settings.BLOOP_SND

    def new_game(self):
        self.all_planets = [objects.Planet(self, 5, (255, 0, 0), [200, 200], [2, -2]),
                            objects.Planet(self, 5, (0, 0, 255), [settings.SCREEN_WIDTH - 200, settings.SCREEN_HEIGHT - 200], [-2, 2])]

        self.all_planets = []

        self.planet_count = len(self.all_planets)

    def add_planet(self):
        angle = math.atan2(self.new_planet_pos[1] - self.mouse_pos[1], self.new_planet_pos[0] - self.mouse_pos[0])
        velocity = math.sqrt((self.new_planet_pos[0] - self.mouse_pos[0])**2 + (self.new_planet_pos[1] - self.mouse_pos[1])**2)
        velocity_vector = [velocity * math.cos(angle), velocity * math.sin(angle)]
        new_planet = objects.Planet(self, self.new_planet_mass, settings.WHITE, self.new_planet_pos, velocity_vector)

        self.all_planets.append(new_planet)

    def update_planets_acceleration(self):
        for n in range(self.planet_count):
            planet = self.all_planets[n]
            planet.sum_forces(self.all_planets)

    def update_planets_position(self):
        for n in range(self.planet_count):
            self.all_planets[n].move()

    def change_time(self, multiplier, change_gravity=True):
        if change_gravity == True:
            self.gravity = multiplier * self.gravity

        for n in range(self.planet_count):
            planet = self.all_planets[n]
            planet.velo_x = multiplier * planet.velo_x
            planet.velo_y = multiplier * planet.velo_y

    def draw_planets(self):
        for n in range(self.planet_count):
            planet = self.all_planets[n]
            pygame.draw.ellipse(self.screen, planet.color, [planet.x - planet.radius, planet.y - planet.radius, 2 * planet.radius, 2 * planet.radius])

    def draw_vectors(self):
        scale = 1
        for n in range(self.planet_count):
            planet = self.all_planets[n]
            pygame.draw.line(self.screen, planet.color, [planet.x, planet.y], [planet.x + planet.velo_x * scale, planet.y + planet.velo_y * scale])

    def draw_ghost(self):
        new_planet_radius = 4 * math.cbrt(self.new_planet_mass) / 3

        pygame.draw.ellipse(self.screen, settings.GHOST_COLOR, [self.new_planet_pos[0] - new_planet_radius, self.new_planet_pos[1] - new_planet_radius,
                                                                2 * new_planet_radius, 2 * new_planet_radius])

        pygame.draw.line(self.screen, settings.GHOST_COLOR, [self.new_planet_pos[0], self.new_planet_pos[1]], [self.mouse_pos[0], self.mouse_pos[1]])

    ### Game Loop
    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False

                elif event.key == pygame.K_r:
                    self.new_game()
                
                elif event.key == pygame.K_SPACE:
                    self.updating = not self.updating

                elif event.key == pygame.K_v:
                    self.showing_vectors = not self.showing_vectors

                elif event.key == pygame.K_LCTRL:
                    self.change_time(0.2, False)

                elif event.key == pygame.K_RCTRL:
                    self.change_time(5, False)

                elif event.key == pygame.K_1:
                    self.new_planet_mass = 1

                elif event.key == pygame.K_0:
                    self.new_planet_mass = 100

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.new_planet_pos = pygame.mouse.get_pos()
                self.drawing_ghost = True

            elif event.type == pygame.MOUSEBUTTONUP:
                self.drawing_ghost = False
                self.add_planet()
        return True

    def update(self):
        self.mouse_pos = pygame.mouse.get_pos()

        if self.updating:
            self.update_planets_acceleration()
            self.update_planets_position()

            self.planet_count = len(self.all_planets)

    def render(self):
        self.screen.fill(settings.BLACK)
        self.draw_planets()

        if self.showing_vectors:
            self.draw_vectors()

        if self.drawing_ghost:
            self.draw_ghost()

    def run(self):
        while self.running:
            self.running = self.process_input()
            self.update()
            self.render()

            pygame.display.update()
            self.clock.tick(settings.FPS)

        pygame.quit()