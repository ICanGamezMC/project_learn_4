import pygame
import math


pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)


running = True


def project(point,width,height,scale, viewer_distance):
    x, y, z = point
    factor = scale / (z + viewer_distance)
    X = int(x *factor + width / 2)
    Y = int(-y *factor + height / 2)
    return (X, Y)


#TEST CUBE POINTS
points = [
    [-1, -1, -1],
    [ 1, -1, -1],
    [ 1,  1, -1],
    [-1,  1, -1],
    [-1, -1,  1],
    [ 1, -1,  1],
    [ 1,  1,  1],
    [-1,  1,  1]
]


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False












