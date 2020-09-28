import numpy
import pygame
from pygame.draw import *

pygame.init()

FPS = 30
WIDTH = 600
HEIGHT = 600
YELLOW = (245, 255, 5)
GRAY = (150, 150, 150)
RED = (255, 10, 10)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# background
rect(screen, GRAY, (0, 0, WIDTH, HEIGHT))

# head
circle(screen, YELLOW, (300, 300), 200)

# eyes
circle(screen, RED, (200, 275), 40)
circle(screen, RED, (400, 275), 30)
circle(screen, BLACK, (200, 275), 15)
circle(screen, BLACK, (400, 275), 15)

# eyebrow
line(screen, BLACK, (270, 276), (110, 111), 30)
line(screen, BLACK, (350, 251), (510, 171), 30)

# mouth
rect(screen, BLACK, (200, 385, 200, 30))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
