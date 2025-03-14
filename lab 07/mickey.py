import pygame
import datetime

pygame.init()
screen = pygame.display.set_mode((800, 600)) 
clock_face = pygame.image.load('clock.png')

minute_hand = pygame.image.load('min_hand.png').convert_alpha()
second_hand = pygame.image.load('sec_hand.png').convert_alpha()

running = True
clock = pygame.time.Clock()
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    now = datetime.datetime.now()
    mins = now.minute
    secs = now.second

    minute_angle = mins * 6 + 53
    second_angle = secs * 6 - 56

    rotated_minute_hand = pygame.transform.rotate(minute_hand, -minute_angle)
    rotated_second_hand = pygame.transform.rotate(second_hand, -second_angle)

    screen.blit(clock_face, (0, 0))

    minute_hand_rect = rotated_minute_hand.get_rect(center=(400, 300))    
    second_hand_rect = rotated_second_hand.get_rect(center=(400, 300))
    screen.blit(rotated_minute_hand, minute_hand_rect)
    screen.blit(rotated_second_hand, second_hand_rect)

    pygame.display.flip()

    clock.tick(30)

pygame.quit()