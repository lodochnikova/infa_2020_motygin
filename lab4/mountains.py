import numpy as np
import pygame
from pygame.draw import *
from LIB_colors import *
from random import randint

pygame.init()

FPS = 30
WIDTH = 800
HEIGHT = 600

BACKCOLORS = [PEACH, PEACH,
              GRAYPEACH, GRAYPEACH,
              YELLOWPEACH, ORANGE,
              WATERBLUE, WATERBLUE, WATERBLUE, WATERBLUE]
BACK_RIDGE = [0.5, -0.5, -0.5, -0.2, -0.4, 0.4, -0.5, -0.5, 0.4, 0.1]
RANDOM_RIDGE = RIDGES[randint(0, 3)]
FRONT_RIDGE = [-0.3, -0.4, 0.0, 0.2]

screen = pygame.display.set_mode((WIDTH, HEIGHT))


def rand_sign():
    return randint(0, 1) * 2 - 1


def dot_array(y_0, height, depth, accelerations):

    res = [(0, y_0)]
    v_x = 1
    if accelerations[0] > 0:
        v_y = -2
    else:
        v_y = 0
    x = 0
    y = y_0

    n = len(accelerations)
    for i in range(n):
        for t in range(WIDTH//n+1):
            v_y += 0.05*accelerations[i]
            if y_0 - y > height and v_y < 0:
                v_y *= -1
            elif y - y_0 > -depth and v_y > 0:
                v_y *= -1
            x += v_x
            y += v_y
            res.append((x, y))

    res.append((x, y_0))

    return res


def setup_background(surface, colors):

    n = len(colors)
    h = HEIGHT/n

    for i in range(n):
        rect(surface, colors[i], (0, i*h, WIDTH, (i+1)*h))


def sun(surface, x, y, radius, color):

    circle(surface, color, (x, y), radius)


def ridge(surface, color, y_0, height, depth, key_array, ):
    mountain_array = dot_array(y_0, height, depth, key_array)

    polygon(surface, color, mountain_array)


def bird(surface, x, y, size, color):
    left_wing = [(x, y), (x - 3 * size, y - 3 * size), (x - 6 * size, y - 2 * size)]
    right_wing = [(x, y), (x + 3 * size, y - 2 * size), (x + 7 * size, y - 1 * size)]

    polygon(surface, color, left_wing)
    polygon(surface, color, right_wing)
    circle(surface, color, (int(x), int(y)), size)


def flock(surface, x, y, color):
    angle = randint(0, 360) / 180 * np.pi

    for i in range(4):
        radius = randint(30, 50)
        size = randint(1, 3) * 2

        bird(surface, x + radius * np.cos(angle), y - radius * np.sin(angle), size, color)

        angle += np.pi/4


def draw():
    setup_background(screen, BACKCOLORS)

    sun(screen, WIDTH//3, HEIGHT//10, HEIGHT//15, YELLOW)

    ridge(screen, ORANGE, 300, 200, 50, BACK_RIDGE)
    ridge(screen, BROWN, 3*HEIGHT//5, 150, 50, RANDOM_RIDGE)
    ridge(screen, DARKEGGPLANT, HEIGHT, 300, 50, FRONT_RIDGE)

    flock(screen, 200, 200, DARKEGGPLANT)
    flock(screen, WIDTH//2, HEIGHT//2, PEACH)
    flock(screen, 600, 400, PEACH)


draw()
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
