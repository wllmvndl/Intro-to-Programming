import pygame

# Window settings
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
TITLE = "My Awesome Game"
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Images
SHIP_IMG = 'assets/images/playerShip.png'
LASER_IMG = 'assets/images/laserBlue.png'
ENEMY_LASER_IMG = 'assets/images/laserRed.png'
FIGHTER_IMG = 'assets/images/enemyRed.png'
BOMBER_IMG = 'assets/images/enemyBlack.png'
ALIEN_IMG = 'assets/images/spaceInvadersAlien.png'
POWERUP_IMG = 'assets/images/powerupYellow_bolt.png'
#MISSILE_IMG = 'assets/images/missile.png'

# Physics
SHIP_SPEED = 5  
LASER_SPEED = 9
POWER_UP_SPEED = 6

RETREAT_SPEED = 3

ENEMY_WIN_SPEED = 3
ENEMY_SHOOT_SPEED = 2.5

# Keys
LEFT = pygame.K_LEFT
RIGHT = pygame.K_RIGHT
SHOOT = pygame.K_SPACE

A_KEY = pygame.K_a
D_KEY = pygame.K_d