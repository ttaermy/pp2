import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))

circle_color = (255, 255, 0)
circle_position = (400, 300)
circle_radius = 25

pygame.draw.circle(screen, circle_color, circle_position, circle_radius)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()