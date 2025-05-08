import pygame
import math

import gravity_pygame_v6
import settings

class Planet(pygame.sprite.Sprite):

    def __init__(self, game, mass, color, position, velocity):
        self.game = game

        self.mass = mass
        self.radius = 2 * math.cbrt(mass)
        self.color = color
        
        self.x = position[0]
        self.y = position[1]

        self.velo_x = velocity[0] / settings.FPS
        self.velo_y = velocity[1] / settings.FPS

        self.acceleration = 0

        self.repel_list = []
        
        self.accl_x = 0
        self.accl_y = 0

        if self.radius > 0:
            self.surface_gravity = self.game.gravity * self.mass / (self.radius)**2
        else:
            self.surface_gravity = 0

    def sum_forces(self, all_planets):
        self.accl_x = 0
        self.accl_y = 0

        for n in range(len(all_planets)):
            self.color = (255, 255, 255)
            other = all_planets[n]
            self.sum_gravity(other)

        for m in range(len(self.repel_list)):
            other = self.repel_list[m]
            accl_angle = math.atan2(self.accl_y, self.accl_x)
            self.acceleration = math.sqrt(self.accl_x**2 + self.accl_y**2)

            angle_normal = math.atan2(other.y - self.y, other.x - self.x)

            force_normal = self.acceleration * math.cos(accl_angle - angle_normal)

            self.accl_x += force_normal * math.cos(angle_normal)
            self.accl_y += force_normal * math.sin(angle_normal)

        self.repel_list = []


    def sum_gravity(self, other):
            if self == other:
                return

            energy_lost = 0.8
            distance = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

            if distance <= (self.radius + other.radius):
                self.repel_list.append(other)
                self.acceleration = 0

            else:
                self.acceleration = self.game.gravity * other.mass / distance ** 2

            angle = math.atan2(other.y - self.y, other.x - self.x)

            self.accl_x += self.acceleration * math.cos(angle)
            self.accl_y += self.acceleration * math.sin(angle)

    def move(self):
        self.velo_x = self.velo_x + self.accl_x
        self.velo_y = self.velo_y + self.accl_y

        self.x += self.velo_x
        self.y += self.velo_y
        
        '''
        if self.x < 0:
            self.x = 0
            self.velo_x = -self.velo_x

        if self.x > settings.SCREEN_WIDTH:
            self.x = settings.SCREEN_WIDTH
            self.velo_x = -self.velo_x

        if self.y < 0:
            self.y = 0
            self.velo_y = -self.velo_y
            
        if self.y > settings.SCREEN_HEIGHT:
            self.y =settings. SCREEN_HEIGHT
            self.velo_y = -self.velo_y
        '''    

    def draw_planet(self):
        pygame.draw.ellipse(self.game.screen, self.color, [self.x - self.radius,
                                                 self.y - self.radius,
                                                 2 * self.radius, 2 * self.radius])
        
    def draw_vector(self):
        pygame.draw.line(self.game.screen, (255, 255, 255), [self.x, self.y],
                         [self.x + self.velo_x * 10, self.y + self.velo_y * 10])
    
    '''
    def update():
        if self in self.game.remove_queue:
            self.kill()
    '''
    
    def update_acceleration(self):
        other = 0
        self.add_accl(other)

    def add_accl(self, other):
        if self == other:
            return 
        
    def update_position(self):
        self.x += self.velo_x
        self.y += self.y