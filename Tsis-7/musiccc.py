import pygame
from pygame import mixer
import os

#REMINDER: Запускать код через путь '...\songsfortask' на терминале

mixer.init()
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Audio Player")
songs = [] 

for song in os.listdir(r'C:\Users\acer\Documents\pp2_springg\Tsis-7\songsfortask'):
    if song.endswith('.mp3'):
        songs.append(song)

# Index of the current song
current_song = 0

mixer.music.load(songs[current_song])

def play_next_song():
    global current_song
    current_song = (current_song + 1) % len(songs)
    mixer.music.load(songs[current_song])
    mixer.music.play()


def play_previous_song():
    global current_song
    current_song = (current_song - 1) % len(songs)
    mixer.music.load(songs[current_song])
    mixer.music.play()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Pause/Unpause
                if mixer.music.get_busy():
                    mixer.music.pause()
                else:
                    mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:  # Next song
                play_next_song()
            elif event.key == pygame.K_LEFT:  # Previous song
                play_previous_song()
            elif event.key == pygame.K_DOWN:  # Stop
                mixer.music.stop()
    pygame.display.flip()
# Quit Pygame
pygame.quit()