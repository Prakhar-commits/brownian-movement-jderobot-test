import numpy as np
import pygame
import matplotlib.pyplot as plt

width = 500
height = 500
robot_position = [width / 2, height / 2]

velocity = [0, 0]
acceleration = [np.random.uniform(-1, 1), np.random.uniform(-1, 1)]


def updated_position(position, velocity, acceleration, friction=0.1):
    velocity[0] += acceleration[0]
    velocity[1] += acceleration[1]
    velocity[0] *= (1 - friction)
    velocity[1] *= (1 - friction)
    position[0] += velocity[0]
    position[1] += velocity[1]

    if position[0] < 0:
        position[0] = 0
        velocity[0] *= -1
    elif position[0] > width:
        position[0] = width
        velocity[0] *= -1
    if position[1] < 0:
        position[1] = 0
        velocity[1] *= -1
    elif position[1] > height:
        position[1] = height
        velocity[1] *= -1
    return position, velocity


pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        robot_position, velocity = updated_position(robot_position, velocity, acceleration)

        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, width, height), 1)
        pygame.draw.circle(screen, (255, 0, 0), (int(robot_position[0]), int(robot_position[1])), 5)

        pygame.display.flip()
        clock.tick(60)
