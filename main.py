import pygame

song = input("Enter the path of the music file...")

pygame.mixer.init()
pygame.mixer.music.load(song)

print("Now playing, " + song)

pygame.mixer.music.play()

input("Press Enter to continue...")