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
font = pygame.font.Font(None, 74)

window = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
pygame.display.set_caption("ALARM TIMER")

def show_time_left(seconds_remaining):
    window.fill(BLACK)
    minutes_remaining = seconds_remaining //60
    seconds_remaining = seconds_remaining % 60
    time_format = f"{minutes_remaining:02d}:{seconds_remaining:02d}"
    text = font.render(time_format, True, WHITE)
    rect_text = text.get_rect(center=(WIDTH_SCREEN // 2, HEIGHT_SCREEN // 2))
    window.blit(text, rect_text)
    pygame.display.flip()
    return time_format

def alarm(seconds):
    time_init = time.time()
    time_elapsed= 0

    while time_elapsed < seconds:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        time_current = time.time()
        time_elapsed = time_current - time_init
        seconds_remaining = int(seconds - time_elapsed)
        show_time_left(seconds_remaining)
        time.sleep(1)

    # PLAY ALARM SOUND
    pygame.mixer.init()
    pygame.mixer.music.load("lofi-alarm-clock-243766.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        time.sleep(1)


minutes= int(input("Enter Minutes: "))
seconds = int (input("Enter seconds: "))
total_seconds = minutes*60+seconds
alarm(total_seconds)




