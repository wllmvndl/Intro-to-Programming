import math
import pygame
import random

import settings

class Ship(pygame.sprite.Sprite):
    
    def __init__(self, game, location):
        super().__init__()
        self.game = game

        self.color = settings.PLAYER_COLOR

        self.x = location[0]
        self.y = location[1]
        self.angle = math.pi / 2

        self.velo_mag = 0
        self.velo_angle = math.pi / 2

        self.shield = 5

        self.fuel = settings.MAX_FUEL


    def check_collisions(self):
        for laser in self.game.lasers:
            if self.color != laser.color:
                distance_to_laser = math.sqrt((self.x - laser.x)**2 + (self.y - laser.y)**2)

                if distance_to_laser < 20:
                    self.shield -= 1
                    laser.kill()

                if self.shield <= 0:
                    self.game.scene = 2

    def move(self):
        self.x += self.velo_mag * math.cos(self.angle)
        self.y += self.velo_mag * math.sin(self.angle)

        if self.x < 0:
            self.x = settings.SCREEN_WIDTH

        if self.x > settings.SCREEN_WIDTH:
            self.x = 0

        if self.y < 0:
            self.y = settings.SCREEN_HEIGHT

        if self.y > settings.SCREEN_HEIGHT:
            self.y = 0

        if self.game.scene == settings.GAME_OVER:
            self.velo_mag *= 0.95

    # Game loop functions
    def process_input(self):
        pressed = pygame.key.get_pressed()

        # Acceleration Magnitude
        if pressed[pygame.K_w]:
            self.velo_mag -= 0.1

        if pressed[pygame.K_s]: # Reverse
            self.velo_mag += 0.1

        if self.fuel > 0 and pressed[pygame.K_RCTRL]:
            self.velo_mag = -12
            self.fuel -= 1 / settings.FPS

        elif self.velo_mag < -8:
            self.velo_mag = -8

        elif self.velo_mag > 3:
            self.velo_mag = 3

        # Rotational Acceleration 
        if pressed[pygame.K_a]: # Left / Clockwise
            self.angle -= settings.PLAYER_ROT_ACCLERATION
            self.velo_angle -= 0.1

        if pressed[pygame.K_d]: # Right / Counterclockwise
            self.angle += settings.PLAYER_ROT_ACCLERATION
            self.velo_angle += 0.1

        if self.velo_angle > 1:
            self.velo_angle = 1
        elif self.velo_angle < 1:
            self.velo_angle = 1

        if not pressed[pygame.K_RCTRL] and self.game.scene == settings.PLAYING:
            if self.fuel < settings.MAX_FUEL:
                self.fuel += 1 / settings.FPS

    def shoot(self):
        if self.game.scene != settings.PLAYING:
            return

        laser = Laser(self.game, [self.x, self.y], self.angle, self.color)
        self.game.lasers.add(laser)

    def update(self):
        self.check_collisions()
        self.move()

    def draw(self, surface):
        self.draw_ship(surface)

        if self.x < settings.CLONE_MARGIN:
            self.draw_ship(surface, settings.SCREEN_WIDTH)

        if self.x > settings.SCREEN_WIDTH - settings.CLONE_MARGIN:
            self.draw_ship(surface, -settings.SCREEN_WIDTH)

        if self.y < settings.CLONE_MARGIN:
            self.draw_ship(surface, 0, settings.SCREEN_HEIGHT)

        if self.y > settings.SCREEN_WIDTH - settings.CLONE_MARGIN:
            self.draw_ship(surface, 0, -settings.SCREEN_HEIGHT)

    def draw_ship(self, surface, offsetx=0, offsety=0):
        sprite_triangle = [[self.x + offsetx - 12 * math.cos(self.angle), self.y + offsety - 12 * math.sin(self.angle)],
                           [self.x + offsetx + 16 * math.sin(self.angle + 1), self.y + offsety - 16 * math.cos(self.angle + 1)],
                           [self.x + offsetx- 16 * math.sin(self.angle - 1), self.y + offsety + 16 * math.cos(self.angle - 1)]]
        
        pygame.draw.polygon(surface, settings.PLAYER_OUTLINE, sprite_triangle, 2)
        pygame.draw.polygon(surface, self.color, sprite_triangle)


        fuel_container = [45, settings.SCREEN_HEIGHT - 135, 45, 90]
        fuel_remaining = [55, settings.SCREEN_HEIGHT - 125 + 70 * (1 - self.fuel / settings.MAX_FUEL),
                          25, 70 * self.fuel / settings.MAX_FUEL]

        pygame.draw.rect(surface, settings.WHITE, fuel_container, 5)
        pygame.draw.rect(surface, self.color, fuel_remaining)

        shield_container = [95, settings.SCREEN_HEIGHT - 135, 45, 90]
        shield_remaining = [105, settings.SCREEN_HEIGHT - 125 + 70 * (1 - self.shield / 5),
                            25, 70 * self.shield / 5]

        pygame.draw.rect(surface, settings.WHITE, shield_container, 5)

        if self.shield > 2:
            pygame.draw.rect(surface, settings.GREEN, shield_remaining)
        elif self.shield > 1:
            pygame.draw.rect(surface, settings.YELLOW, shield_remaining)
        else:
            pygame.draw.rect(surface, settings.RED, shield_remaining)

class Laser(pygame.sprite.Sprite):

    def __init__(self, game, location, angle, color=settings.WHITE):
        super().__init__()

        self.game = game
        self.color = color

        self.lifespan = 5 * settings.FPS

        self.x = location[0]
        self.y = location[1]

        self.angle = angle

    def move(self):
        self.x -= settings.LASER_SPEED * math.cos(self.angle)
        self.y -= settings.LASER_SPEED * math.sin(self.angle)

    def lose_energy(self):
        self.lifespan -= 1

        if self.lifespan <= 0:
            self.kill()

    def update(self):
        self.move()
        self.lose_energy()

    def draw(self, surface):
        self.draw_laser(surface)

    def draw_laser(self, surface, offsetx=0, offsety=0):
        radius = 8
        pygame.draw.ellipse(surface, self.color, [self.x + offsetx, self.y + offsety, radius, radius])

class Enemy(pygame.sprite.Sprite):

    def __init__(self, game, location, angle, color=settings.RED, shield=1):
        super().__init__()
        
        self.game = game

        self.color = color
        self.shield = shield

        self.x = location[0]
        self.y = location[1]
        self.angle = angle

        self.speed = 0

    def check_collisions(self):
        for laser in self.game.lasers:
            if self.color != laser.color:
                distance_to_laser = math.sqrt((self.x - laser.x)**2 + (self.y - laser.y)**2)

                if distance_to_laser < 20:
                    self.shield -= 1
                elif distance_to_laser < 75:
                    self.color = settings.WHITE
                else:
                    self.color = settings.RED

                if self.shield <= 0:
                    self.kill()
                    laser.kill()
                    self.game.score += 100
                    self.game.explosions.add(Explosions(self))

        for enemy in self.game.enemies:
            if self != enemy:
                distance_to_other = math.sqrt((self.x - enemy.x)**2 + (self.y - enemy.y)**2)

                if distance_to_other < 50:
                    self.angle += 0.3
                    enemy.angle -= 0.3

    def turn(self):
        delta_angle = -math.sin(self.angle - math.atan2(self.game.ship.y - self.y, self.game.ship.x - self.x))
        self.angle -= 3 * delta_angle / settings.FPS

    def move(self):
        distance = math.sqrt((self.x - self.game.ship.x)**2 + (self.x - self.game.ship.x)**2)

        self.speed += (distance / settings.SCREEN_WIDTH) ** 2
        if self.speed > settings.ENEMY_VELOCITY:
            self.speed = settings.ENEMY_VELOCITY

        self.x -= self.speed * math.cos(self.angle)
        self.y -= self.speed * math.sin(self.angle)

        if self.x < 0:
            self.x = settings.SCREEN_WIDTH

        if self.x > settings.SCREEN_WIDTH:
            self.x = 0

        if self.y < 0:
            self.y = settings.SCREEN_HEIGHT

        if self.y > settings.SCREEN_HEIGHT:
            self.y = 0

    def shoot(self):
        if self.game.scene != settings.PLAYING:
            return

        r = random.uniform(0, settings.FPS)
        if r > 0.5:
            return

        laser = Laser(self.game, [self.x, self.y], self.angle, self.color)
        self.game.lasers.add(laser)

    def update(self):
        self.check_collisions()
        self.turn()
        self.move()
        self.shoot()

    def draw(self, surface):
        self.draw_ship(surface)

        if self.x < settings.CLONE_MARGIN:
            self.draw_ship(surface, settings.SCREEN_WIDTH)

        if self.x > settings.SCREEN_WIDTH - settings.CLONE_MARGIN:
            self.draw_ship(surface, -settings.SCREEN_WIDTH)

        if self.y < settings.CLONE_MARGIN:
            self.draw_ship(surface, 0, settings.SCREEN_HEIGHT)

        if self.y > settings.SCREEN_HEIGHT - settings.CLONE_MARGIN:
            self.draw_ship(surface, 0, -settings.SCREEN_HEIGHT)

    def draw_ship(self, surface, offsetx=0, offsety=0):
        sprite_triangle = [[self.x + offsetx - 12 * math.cos(self.angle), self.y + offsety - 12 * math.sin(self.angle)],
                           [self.x + offsetx + 16 * math.sin(self.angle + 1), self.y + offsety - 16 * math.cos(self.angle + 1)],
                           [self.x + offsetx- 16 * math.sin(self.angle - 1), self.y + offsety + 16 * math.cos(self.angle - 1)]]
        
        pygame.draw.polygon(surface, self.color, sprite_triangle)

class Star(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()

        self.game = game
        self.x = random.randint(0, settings.SCREEN_WIDTH)
        self.y = random.randint(0, settings.SCREEN_HEIGHT)
        self.base_radius = random.randint(1, 2)
        self.radius = self.base_radius
        self.multipler = 1

        self.star_rect = [self.x - self.radius, self.y - self.radius, 2 * self.radius, 2 * self.radius]

    def get_color(self):
        pressed = pygame.key.get_pressed()

        if self.game.scene == settings.GAME_OVER:
            if self.multipler > 0.02:
                self.multipler -= 0.02
            else:
                self.multipler = 0

        elif pressed[pygame.K_RCTRL]:
            self.multipler = 1.275
        else:
            self.multipler = 1

        return (200 * self.multipler, 200 * self.multipler, 200 * self.multipler)

    def draw(self, surface):
        pygame.draw.ellipse(surface, self.get_color(), self.star_rect)

class Explosions(pygame.sprite.Sprite):

    def __init__(self, ship):
        super().__init__()

        self.lifespan = settings.EXPLOSION_LIFESPAN
        self.x = ship.x
        self.y = ship.y

    def get_color(self):
        r = 255 * (self.lifespan / settings.EXPLOSION_LIFESPAN)
        g = 255 * (self.lifespan / settings.EXPLOSION_LIFESPAN) ** 2
        b = 255 * (self.lifespan / settings.EXPLOSION_LIFESPAN) ** 3
        return (r, g, b)
    
    def get_rect(self):
        radius = 20 * (self.lifespan / settings.EXPLOSION_LIFESPAN) ** 2
        circle_rect = [self.x - radius, self.y - radius, 2 * radius, 2 * radius]
        return circle_rect
    
    def update(self):
        self.lifespan -= 1

        if self.lifespan <= 0:
            self.kill()

    def draw(self, surface):
        pygame.draw.ellipse(surface, self.get_color(), self.get_rect())