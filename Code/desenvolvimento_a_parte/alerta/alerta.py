import pygame
sound = 'Yamete.mp3'
pygame.init()
pygame.mixer.music.load('sounds/'+ sound)
pygame.mixer.music.play()
pygame.event.wait()
