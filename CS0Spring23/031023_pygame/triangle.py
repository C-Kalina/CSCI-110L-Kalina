# pick a point
# randomly choose a vertix of the triangle
# plot a point halfway between the triangle vertix and the original position
# from the new position, repeat

import pygame
import random

pygame.init()
width = 1000
height = 600
iterations = 10

window = pygame.display.set_mode((width, height))
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if(event.key == pygame.K_ESCAPE):
                run = False

    for i in range(iterations):
        color = (0,255,0)
        window.set_at((100, 100), color)
    
    pygame.display.flip()

pygame.quit()
exit()