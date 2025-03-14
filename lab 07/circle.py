import pygame
import sys

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

circle_color = (255, 255, 0)
circle_position = [400, 300]
circle_radius = 25
move_amount = 20

def movement(dx, dy):
    global circle_position
    new_x = circle_position[0] + dx
    new_y = circle_position[1] + dy

    if 0 <= new_x <= width and 0 <= new_y <= height:
        circle_position[0] = new_x
        circle_position[1] = new_y


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:  
                movement(0, -move_amount)
            elif event.key == pygame.K_DOWN: 
                movement(0, move_amount)
            elif event.key == pygame.K_LEFT:
                movement(-move_amount, 0)
            elif event.key == pygame.K_RIGHT:
                movement(move_amount, 0)

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, circle_color, circle_position, circle_radius)

    pygame.display.flip()

pygame.quit()
sys.exit()