import random
import math
import pygame
import settings

class Entity(pygame.sprite.Sprite):

    def __init__(self, game, image, location):
        super().__init__()

        self.game = game
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = location


class Ship(Entity):

    def __init__(self, game, image, location):
        super().__init__(game, image, location)

        self.shield = 3
        self.immunity_timer = 0

    def move_left(self):
        self.rect.x -= settings.SHIP_SPEED

    def move_right(self):
        self.rect.x += settings.SHIP_SPEED

    def shoot(self):
        if self.shield <= 0:
            return

        laser = Laser(self.game, self.game.laser_img, self.rect.midtop)
        self.game.lasers.add(laser)

    def check_collisions(self):
        hits = pygame.sprite.spritecollide(self, self.game.powerups, True)

        if len(hits) > 0:
            if random.randint(0, 1) == 0:
                self.shield += 1
            else:
                self.immunity_timer += 3 * settings.FPS

        if self.immunity_timer > 0:
            self.immunity_timer -= 1

        hits = pygame.sprite.spritecollide(self, self.game.enemy_lasers, True)
    
        if self.immunity_timer == 0:
            self.shield -= len(hits)

        if self.shield <= 0:
            self.retreat()
            self.game.scene = 2

    def retreat(self):
        self.rect.y += 15

        if self.rect.top > settings.SCREEN_HEIGHT:
            self.kill()

    def move(self):
        if self.shield <= 0:
            return

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > settings.SCREEN_WIDTH:
            self.rect.right = settings.SCREEN_WIDTH

    def update(self):
        self.check_collisions()
        self.move()

class Enemy(Entity):

    def __init__(self, game, image, location, shield=2):
        super().__init__(game, image, location)
        self.rect.y -= 250
        self.formation_y = self.rect.y + 250
        self.in_position = False

        self.vx = 2.5
        self.shield = shield

    def move_into_position(self):
        if self.in_position == True:
            return

        if self.rect.y < self.formation_y:
            self.rect.y += 5

        if self.rect.y >= self.formation_y:
            self.rect.y = self.formation_y
            self.in_position = True

    def move(self):
        if self.in_position == False or self.shield <= 0:
            return

        for enemy in self.game.enemies:
            if enemy.rect.left < 0 or enemy.rect.right > settings.SCREEN_WIDTH:
                self.vx *= -1

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > settings.SCREEN_WIDTH:
            self.rect.right = settings.SCREEN_WIDTH
        
        self.rect.x += self.vx

    def advance(self):
        if self.game.scene == 2 and self.shield > 0:
            self.rect.y += settings.ENEMY_WIN_SPEED * (1 + 6 * self.rect.top / settings.SCREEN_HEIGHT)

            if self.rect.top > settings.SCREEN_HEIGHT:
                self.kill()

    def retreat(self):
        self.rect.y -= settings.RETREAT_SPEED

        if self.rect.bottom < 0:
            self.kill()

    def check_lasers(self):
        hits = pygame.sprite.spritecollide(self, self.game.lasers, True)

        self.shield -= len(hits)

        if self.shield <= 0:
            self.retreat()

    def shoot(self):
        if self.game.scene != 1 or len(self.game.enemies) == 0 or self.shield <= 0:
            return

        r = random.uniform(0, settings.FPS)
        random_offset = random.randint(-10, 10)

        '''
        if self.image == self.game.bomber_img and r < settings.BOMBER_MISSILE_SHOOT:
            missile = Missile(self.game, self.game.missile_img, [self.rect.midbottom[0] + random_offset, self.rect.bottom])
            self.game.missiles.add(missile)
        '''
        
        if r < settings.ENEMY_SHOOT_SPEED / math.cbrt(len(self.game.enemies)):
            laser = EnemyLaser(self.game, self.game.enemy_laser_img, [self.rect.midbottom[0] + random_offset, self.rect.bottom])
            self.game.enemy_lasers.add(laser)


    def update(self):
        self.move_into_position()
        self.move()
        self.check_lasers()
        self.shoot()
        self.advance()


class Laser(pygame.sprite.Sprite):

    def __init__(self, game, image, location):
        super().__init__()

        self.game = game
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = location

    def move(self):
        self.rect.y -= settings.LASER_SPEED

        if self.rect.bottom < 0:
            self.kill()

    def check_lasers(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemy_lasers, True)

        if len(hits) > 0:
            self.kill()

    def update(self):
        self.move()
        self.check_lasers()


class EnemyLaser(pygame.sprite.Sprite):

    def __init__(self, game, image, location):
        super().__init__()

        self.game = game
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = location

    def update(self):
        self.rect.y += settings.LASER_SPEED

        if self.game.scene == 2:
            self.rect.y += settings.ENEMY_WIN_SPEED * (1 + 6 * self.rect.top / settings.SCREEN_HEIGHT)

        if self.rect.top > settings.SCREEN_HEIGHT:
            self.kill()

class Powerup(pygame.sprite.Sprite):

    def __init__(self, game, image, location):
        super().__init__()

        self.game = game
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = location

    def update(self):
        self.rect.y += settings.POWER_UP_SPEED

        if self.rect.top > settings.SCREEN_HEIGHT:
            self.kill()