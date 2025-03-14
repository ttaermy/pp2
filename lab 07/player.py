import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 300)) 
pygame.display.set_caption("Music Player")

pygame.mixer.init()

songs = ["1.mp3", "2.mp3", "3.mp3"]
cur_index = 0

pygame.mixer.music.load(songs[cur_index])

def play_next_song():
    global cur_index
    cur_index = (cur_index + 1) % len(songs)
    pygame.mixer.music.load(songs[cur_index])
    pygame.mixer.music.play()

def play_previous_song():
    global cur_index
    cur_index = (cur_index - 1) % len(songs)
    pygame.mixer.music.load(songs[cur_index])
    pygame.mixer.music.play()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:  
                play_next_song()
            elif event.key == pygame.K_p: 
                play_previous_song()
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
            elif event.key == pygame.K_c:
                pygame.mixer.music.play()


pygame.quit()
sys.exit()