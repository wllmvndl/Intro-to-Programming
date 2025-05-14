import math
import pygame
import random

import settings
import entities

class Game:

    def __init__(self):
        # Initialize pygame
        pygame.mixer.pre_init()
        pygame.init()

        # Make window
        self.screen = pygame.display.set_mode([settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT])
        pygame.display.set_caption(settings.TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

        # Set up game
        self.scene = settings.START
        self.load_assets()
        self.new_game()

        self.score = 0

        self.level = 0
        self.grace_period = 0
        self.shield = 3

    def load_assets(self):
        self.title_font = pygame.font.Font(None, 96)
        self.hud_font = pygame.font.Font(None, 36)

    def new_game(self):
        self.players = pygame.sprite.Group()
        self.lasers = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()

        for _ in range(350):
            self.stars.add(entities.Star(self))

        self.ship = entities.Ship(self, [settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT - 100])
        self.players.add(self.ship)

    def check_cleared(self):
        if self.scene != settings.PLAYING:
            return

        if len(self.enemies) == 0 and self.grace_period == 0:
            self.grace_period += 1.5 * settings.FPS
            self.level += 1
            self.ship.shield += 2

        if self.ship.shield > 5:
            self.ship.shield = 5

        if len(self.enemies) == 0 and self.grace_period == 1:
            self.add_enemies(math.floor(10 * math.exp(self.level / 10)))

        if self.grace_period > 0:
            self.grace_period -= 1

    def add_enemies(self, enemies):
        for _ in range(enemies):
            enemy = entities.Enemy(self, [random.randint(0, settings.SCREEN_WIDTH), random.randint(0, settings.SCREEN_HEIGHT)], random.uniform(0, 2 * math.pi))
            self.enemies.add(enemy)

    def show_hud(self):
        if self.scene == settings.PLAYING:
            text = self.hud_font.render(f'Enemies Remaining: {len(self.enemies)}', True, settings.WHITE)
            rect = text.get_rect()
            rect.bottomright = [settings.SCREEN_WIDTH - 20, settings.SCREEN_HEIGHT - 20]
            self.screen.blit(text, rect)

            text = self.hud_font.render(f'Score: {self.score}', True, settings.WHITE)
            rect = text.get_rect()
            rect.topright = [settings.SCREEN_WIDTH - 20, 20]
            self.screen.blit(text, rect)

        if self.grace_period > 0:
            text = self.title_font.render(f'{int(self.grace_period // 30) + 1}', True, settings.WHITE)
            rect = text.get_rect()
            rect.center = [settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT / 2]
            self.screen.blit(text, rect)

        if self.scene == settings.GAME_OVER:
            text = self.hud_font.render(f'Score', True, settings.WHITE)
            rect = text.get_rect()
            rect.midbottom = [settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT / 2 - 15]
            self.screen.blit(text, rect)

            text = self.title_font.render(f'{self.score}', True, settings.WHITE)
            rect = text.get_rect()
            rect.midtop = [settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT / 2 - 15]
            self.screen.blit(text, rect)

    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

                if event.key == pygame.K_SPACE:
                    if self.scene == settings.START:
                        self.scene = settings.PLAYING
                    else:
                        self.ship.shoot()

                if event.key == pygame.K_r:
                    self.new_game()
                    self.scene = settings.START

                if event.key == pygame.K_0:
                    self.add_enemies(15)

        if self.scene == settings.PLAYING:
            self.ship.process_input()

    def update(self):
        self.check_cleared()

        self.explosions.update()
        self.ship.update()
        self.enemies.update()
        self.lasers.update()

    def pg_draw(self, group):
        for object in group:
            object.draw(self.screen)

    def render(self):
        self.screen.fill(settings.BLACK)

        self.pg_draw(self.stars)
        
        self.ship.draw(self.screen)
        
        self.pg_draw(self.enemies)
        self.pg_draw(self.lasers)
        self.pg_draw(self.explosions)

        self.show_hud()

    def run(self):
        while self.running:
            self.process_input()     
            self.update()
            self.render()
            
            pygame.display.update()
            self.clock.tick(settings.FPS)

        pygame.quit()