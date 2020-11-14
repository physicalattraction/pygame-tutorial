import os.path

import pygame
from pygame.locals import *

size = 640, 620
width, height = size
GREEN = (150, 255, 150)
RED = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode(size)
running = True

path_to_gif = os.path.join('..', 'resources', 'ball.gif')
ball = pygame.image.load(path_to_gif)
rect = ball.get_rect()
speed = [0, 0]

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    rect = rect.move(speed)
    if rect.left < 0 or rect.right > width:
        speed[0] = -speed[0]
    if rect.top < 0 or rect.bottom > height:
        speed[1] = -speed[1]

    speed[1] += 0.02

    print(speed)
    screen.fill(GREEN)
    pygame.draw.rect(screen, RED, rect, 1)
    screen.blit(ball, rect)
    pygame.display.update()

pygame.quit()
