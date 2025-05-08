import pygame

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

CAPTION = "2D Gravity Simulator"
FPS = 60

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

GHOST_COLOR = (200, 220, 255)

# sounds
pygame.init()

CLACK_SND = pygame.mixer.Sound('assets/sounds/clack.ogg')
SONAR_SND = pygame.mixer.Sound('assets/sounds/sonar.ogg')
BLOOP_SND = pygame.mixer.Sound('assets/sounds/bloop.ogg')