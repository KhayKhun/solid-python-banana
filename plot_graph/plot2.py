# y = x^2
import pygame
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
logger.info("Program started")

def f(x):
    return x**2

pygame.init()

w = 600
h = 600

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Draw graph")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    screen.fill((0, 0, 0))

    prev_x = None
    prev_y = None

    for x in range(w):

        actual_x = x * (1/150) - 2
        actual_y = f(actual_x)

        screen_y = h - int(actual_y * 150) - 1

        screen.set_at((x, screen_y), (255, 255, 255))

        if prev_x:
            pygame.draw.line(screen, (255, 255, 255), (x, screen_y), (prev_x, prev_y))

        prev_x = x
        prev_y = screen_y


    pygame.display.flip()

pygame.quit()