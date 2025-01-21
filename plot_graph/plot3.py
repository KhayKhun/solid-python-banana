import pygame
import math
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
logger.info("Program started")

def f(x):
    return math.sin(x)

pygame.init()

w = 600
h = 600

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Draw sin(x) Graph")

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
        actual_x = (x / w) * (4 * math.pi) - (2 * math.pi)  # map x from 0-600 to -2π to 2π
        actual_y = f(actual_x)

        screen_y = h // 2 - int(actual_y * (h // 3))  # scale sin(x) to fit within screen

        screen.set_at((x, screen_y), (255, 255, 255))

        if prev_x:
            pygame.draw.line(screen, (255, 255, 255), (x, screen_y), (prev_x, prev_y))

        prev_x = x
        prev_y = screen_y

    pygame.display.flip()

pygame.quit()