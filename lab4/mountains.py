import numpy
import pygame
from pygame.draw import *
from LIB_colors import *

pygame.init()

FPS = 30
WIDTH = 800
HEIGHT = 600

BACKCOLORS = [PEACH, GRAYPEACH, YELLOWPEACH, EGGPLANT, EGGPLANT]
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# background
N = len(BACKCOLORS)
h = HEIGHT/N
for i in range(N):
    rect(screen, BACKCOLORS[i], (0, i*h, WIDTH, (i+1)*h))

aaline(screen, BLACK, (100, 100), (150, 200))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
