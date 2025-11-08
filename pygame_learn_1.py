import pygame
import math

#This is starting up variables / initializers
pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True


angle = 0
background_color = (0,0,0)

#This is projection mapping
def project(point,width,height,scale, viewer_distance):
    x, y, z = point
    factor = scale / (z + viewer_distance)
    X = int(x *factor + width / 2)
    Y = int(-y *factor + height / 2)
    return (X, Y)

def rotateY(point, angle):
    x, y, z = point
    rad = math.radians(angle)
    cos, sin = math.cos(rad), math.sin(rad)
    X = x * cos - z * sin
    Z = x * sin + z * cos
    return(X,y,Z)



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


#This is the main func for everything
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    angle += 1  # increment rotation once per frame

    #This rotates the points
    rotated_points = []
    for point in points:
        rotated = rotateY(point, angle)
        rotated_points.append(rotated)

    #This projects points based on rotation beforehand
    for rotated in rotated_points:
        x, y = project(rotated, width, height, 256, 4)
        pygame.draw.circle(screen, (255, 255, 255), (x, y), 3)

    
    

    #This updates displays
    pygame.display.flip()
    screen.fill(background_color)
    clock.tick(60)










