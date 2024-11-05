import time
import pygame
import sys

# Iniciar pygame y mixer
pygame.init()
pygame.mixer.init()

# Configuración de pantalla
WIDTH_SCREEN = 640
HEIGHT_SCREEN = 480

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

# Fuente
font_large = pygame.font.Font(None, 74)
font_small = pygame.font.Font(None, 36)

window = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
pygame.display.set_caption("ALARM TIMER")

# Clock para controlar FPS
clock = pygame.time.Clock()

def show_time_left(seconds_remaining):
    window.fill(BLACK)
    minutes_remaining = seconds_remaining // 60
    seconds_remaining = seconds_remaining % 60
    time_format = f"{minutes_remaining:02d}:{seconds_remaining:02d}"
    text = font_large.render(time_format, True, WHITE)
    rect_text = text.get_rect(center=(WIDTH_SCREEN // 2, HEIGHT_SCREEN // 2))
    window.blit(text, rect_text)
    pygame.display.flip()
    return time_format

def alarm(seconds):
    time_init = time.time()
    time_elapsed = 0

    while time_elapsed < seconds:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Actualiza el tiempo
        time_current = time.time()
        time_elapsed = time_current - time_init
        seconds_remaining = int(seconds - time_elapsed)
        show_time_left(seconds_remaining)

        # Limita el bucle a 1 vez por segundo para evitar parpadeos
        clock.tick(1)

    # Reproduce sonido de alarma
    try:
        pygame.mixer.music.load("lofi-alarm-clock-243766.mp3")
        pygame.mixer.music.play()
    except pygame.error as e:
        print("Error al cargar el sonido:", e)
        return

    # Espera a que termine la música o a que se cierre la ventana
    while pygame.mixer.music.get_busy():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        clock.tick(1)  # Reduce la carga del loop de espera

def input_time():
    user_input = ""
    active_input = True
    while active_input:
        window.fill(BLACK)

        # Mensaje de instrucciones
        message = "Enter time in MM:SS format"
        text_message = font_small.render(message, True, WHITE)
        rect_message = text_message.get_rect(center=(WIDTH_SCREEN // 2, HEIGHT_SCREEN // 3))
        window.blit(text_message, rect_message)

        # Cuadro de entrada de texto
        text_surface = font_large.render(user_input, True, WHITE)
        input_rect = pygame.Rect(WIDTH_SCREEN // 2 - 100, HEIGHT_SCREEN // 2 - 30, 200, 60)
        pygame.draw.rect(window, GRAY, input_rect)
        window.blit(text_surface, (input_rect.x + 10, input_rect.y + 10))

        pygame.display.flip()

        # Manejo de eventos para la entrada de texto
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    active_input = False
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode

        clock.tick(30)

    # Procesar el tiempo ingresado en formato MM:SS
    try:
        minutes, seconds = map(int, user_input.split(":"))
        total_seconds = minutes * 60 + seconds
        return total_seconds
    except ValueError:
        print("Error: formato incorrecto. Asegúrate de ingresar en formato MM:SS")
        return None

# Programa principal
def main():
    total_seconds = input_time()
    if total_seconds:
        alarm(total_seconds)
    else:
        print("No se configuró un tiempo válido.")

main()
