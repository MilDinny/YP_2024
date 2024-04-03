import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))
polygon(screen, (245, 245, 220), [(0,0), (0,125), (600,125), (600,0)])
polygon(screen, (230, 230, 250), [(0,125), (0,250), (600,250), (600,125)])
polygon(screen, (255, 205, 125), [(0,250), (0,375), (600,375), (600,250)])
circle(screen, (255, 255, 0), (300, 125), 42)
polygon(screen, (255, 165, 0), [(0, 265), (10, 235), (18, 245), (100, 115), (125, 125), (130, 140), (240, 220), (285, 208), (310, 220), (340, 190), (360, 200), (385, 182), (415, 188), (480, 100), (495, 105), (515, 140), (522, 130), (543, 172), (567, 165), (600, 185)])
polygon(screen, (138, 51, 36), [(0, 280), (5, 280), (95, 370), (123, 315), (168, 345), (185, 290), (242, 304), (292, 335), (348, 319), (368, 300), (420, 240), (434, 248), (450, 262), (465, 270), (486, 310), (510, 280), (532, 295), (548, 276), (570, 280), (600, 200), (600, 375), (0, 405)])
ellipse(screen, (138, 51, 36), (0, 230, 115, 270))
polygon(screen, (201, 174, 250), [(0,375), (0,600), (600,600), (600,375)])
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()