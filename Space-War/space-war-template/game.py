# Imports
import pygame

import entities
import settings

# Main game class 
class Game:
    
    # Scenes
    START = 0
    PLAYING = 1
    LOSE = 2
    
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
        self.load_assets()
        self.new_game()

    def load_assets(self):
        self.title_font = pygame.font.Font('assets/fonts/recharge_bd.ttf', 64)
        self.subtitle_font = pygame.font.Font('assets/fonts/recharge_bd.ttf', 32)

        self.ship_img = pygame.image.load(settings.SHIP_IMG).convert_alpha()
        self.laser_img = pygame.image.load(settings.LASER_IMG).convert_alpha()
        self.enemy_laser_img = pygame.image.load(settings.ENEMY_LASER_IMG).convert_alpha()
        self.fighter_img = pygame.image.load(settings.FIGHTER_IMG).convert_alpha()
        self.bomber_img = pygame.image.load(settings.BOMBER_IMG).convert_alpha()
        self.alien_img = pygame.image.load(settings.ALIEN_IMG).convert_alpha()
        self.powerup_img = pygame.image.load(settings.POWERUP_IMG).convert_alpha()
        #self.missile_img = pygame.image.load(settings.MISSILE_IMG).convert_alpha()

    def new_game(self):
        self.level = 0
        self.grace_period = 0.5 * settings.FPS

        self.player = pygame.sprite.Group()
        self.lasers = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.enemy_lasers = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()
        self.missiles = pygame.sprite.Group()

        self.ship = entities.Ship(self, self.ship_img, [settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT - 100])
        self.player.add(self.ship)

        self.scene = Game.START
        self.load_current_level()

    def load_current_level(self):
        if self.level == 0:
            e1 = entities.Enemy(self, self.fighter_img, [settings.SCREEN_WIDTH / 2, 100])
            self.enemies.add(e1)

        elif self.level == 1:
            e1 = entities.Enemy(self, self.bomber_img, [settings.SCREEN_WIDTH / 2, 150], 3)
            e2 = entities.Enemy(self, self.fighter_img, [settings.SCREEN_WIDTH / 2 - 200, 100])
            e3 = entities.Enemy(self, self.fighter_img, [settings.SCREEN_WIDTH / 2 + 200, 100])
            self.enemies.add(e1, e2, e3)

        elif self.level == 2:
            e1 = entities.Enemy(self, self.alien_img, [settings.SCREEN_WIDTH / 2, 200], 4)
            e2 = entities.Enemy(self, self.alien_img, [settings.SCREEN_WIDTH / 2 + 100, 100])
            e3 = entities.Enemy(self, self.alien_img, [settings.SCREEN_WIDTH / 2 - 100, 100])
            e4 = entities.Enemy(self, self.fighter_img, [settings.SCREEN_WIDTH / 2 + 300, 100])
            e5 = entities.Enemy(self, self.fighter_img, [settings.SCREEN_WIDTH / 2 - 300, 100])
            self.enemies.add(e1, e2, e3, e4, e5)
            self.powerups.add(entities.Powerup(self, self.powerup_img, [settings.SCREEN_WIDTH / 2, -300]))

        elif self.level >= 3:
            e5 = entities.Enemy(self, self.bomber_img, [settings.SCREEN_WIDTH / 2 - 400, 100], 3)
            e1 = entities.Enemy(self, self.fighter_img, [settings.SCREEN_WIDTH / 2 - 200, 100])
            e2 = entities.Enemy(self, self.fighter_img, [settings.SCREEN_WIDTH / 2, 100])
            e3 = entities.Enemy(self, self.fighter_img, [settings.SCREEN_WIDTH / 2 + 200, 100])
            e4 = entities.Enemy(self, self.bomber_img, [settings.SCREEN_WIDTH / 2 + 400, 100], 3)
            e6 = entities.Enemy(self, self.alien_img, [settings.SCREEN_WIDTH / 2 + 100, 200], 3)
            e7 = entities.Enemy(self, self.alien_img, [settings.SCREEN_WIDTH / 2 - 100, 200], 3)
            self.enemies.add(e1, e2, e3, e4, e5, e6, e7)
            self.powerups.add(entities.Powerup(self, self.powerup_img, [settings.SCREEN_WIDTH / 2, -300]))

    def play(self):
        self.scene = Game.PLAYING

    def lose(self):
        self.scene = Game.LOSE

    def show_title_screen(self):
        text = self.title_font.render(settings.TITLE, True, settings.WHITE)
        rect = text.get_rect()
        rect.midbottom = settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT // 2 - 8
        self.screen.blit(text, rect)
    
        text = self.subtitle_font.render("Press 'SPACE' to start.", True, settings.WHITE)
        rect = text.get_rect()
        rect.midtop = settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT // 2 + 8
        self.screen.blit(text, rect)

    def show_hud(self):
        text = self.subtitle_font.render("Level: " + str(self.level), True, settings.WHITE)
        rect = text.get_rect()
        rect.left = 20
        rect.bottom = settings.SCREEN_HEIGHT - 20
        self.screen.blit(text, rect)

        if self.ship.immunity_timer > 0:
            text = self.subtitle_font.render(f"Immunity: {self.ship.immunity_timer // 60 + 1}", True, settings.WHITE)
            rect = text.get_rect()
            rect.left = 20
            rect.bottom = settings.SCREEN_HEIGHT - 50
            self.screen.blit(text, rect)

        text = self.subtitle_font.render("Shield: " + str(self.ship.shield), True, settings.WHITE)
        rect = text.get_rect()
        rect.right = settings.SCREEN_WIDTH - 20
        rect.bottom = settings.SCREEN_HEIGHT - 20
        self.screen.blit(text, rect)

    def show_end_screen(self):
        text = self.title_font.render("Game over", True, settings.WHITE)
        rect = text.get_rect()
        rect.midbottom = settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT // 2 - 8
        self.screen.blit(text, rect)
    
        text = self.subtitle_font.render("Press 'r' to play again.", True, settings.WHITE)
        rect = text.get_rect()
        rect.midtop = settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT // 2 + 8
        self.screen.blit(text, rect)

    def check_cleared(self):
        if self.scene != 1:
            return

        if len(self.enemies) == 0:
            if self.grace_period == 0:
                self.grace_period = 0.5 * settings.FPS
            else:
                self.grace_period -= 1

        if self.grace_period == 1:
            self.level += 1
            self.load_current_level()
            self.grace_period = 0

    def process_input(self):
        pressed = pygame.key.get_pressed()
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

                if self.scene == Game.START:
                    if event.key == pygame.K_SPACE:
                        self.play()

                elif self.scene == Game.PLAYING:
                    if event.key == pygame.K_SPACE:
                        self.ship.shoot()

                elif self.scene == Game.LOSE:
                    if event.key == pygame.K_r:
                        self.__init__()

        if self.scene == Game.PLAYING:
            if pressed[settings.LEFT] or pressed[settings.A_KEY]:
                self.ship.move_left()
            elif pressed[settings.RIGHT] or pressed[settings.D_KEY]:
                self.ship.move_right()

    def update(self):
        self.check_cleared()

        self.player.update()
        self.lasers.update()
        self.enemies.update()
        self.enemy_lasers.update()
        self.powerups.update()
        self.missiles.update()

    def render(self):
        self.screen.fill(settings.BLACK)

        self.lasers.draw(self.screen)
        self.enemy_lasers.draw(self.screen)
        self.missiles.draw(self.screen)

        self.powerups.draw(self.screen)
        self.enemies.draw(self.screen)

        self.player.draw(self.screen)

        if self.scene == Game.START:
            self.show_title_screen()
        
        elif self.scene == Game.PLAYING:
            self.show_hud()

        elif self.scene == Game.LOSE:
            self.show_end_screen()
        
    def run(self):
        while self.running:
            self.process_input()     
            self.update()     
            self.render()
            
            pygame.display.update()
            self.clock.tick(settings.FPS)

        pygame.quit()
