import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((255, 255, 255))
circle(screen, (255, 255, 0), (200, 175), 100)
circle(screen, (0, 0, 0), (160, 150), 21)
circle(screen, (255, 0, 0), (160, 150), 20)
circle(screen, (0, 0, 0), (160, 150), 9)
circle(screen, (0, 0, 0), (240, 150), 15)
circle(screen, (255, 0, 0), (240, 150), 14)
circle(screen, (0, 0, 0), (240, 150), 7)
line(screen, (0, 0, 0), (155, 230), (245, 230), 20)
line(screen, (0, 0, 0), (190, 138), (100, 88), 10)
line(screen, (0, 0, 0), (210, 138), (280, 110), 10)
pygame.display.flip()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()