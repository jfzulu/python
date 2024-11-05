import time
import pygame
import sys

#Iniciar pygame
pygame.init()

#Configure screen
WIDTH_SCREEN = 640
HEIGHT_SCREEN = 480

#COLORS
BLACK = (0, 0 , 0)
WHITE = (255, 255, 255)

#FONT
font = pygame.font.Font("Arial", 74)

window = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
pygame.display.set_caption("ALARM TIMER")

def show_time_left(Seconds_remaining)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()