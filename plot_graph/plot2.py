# y = x^2
import pygame
import math
import random
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
logger.info("Program started")

def f(x):
    return x**2

pygame.init()
w = 600
h = 600

sample_count = 60

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Draw graph")

running = True

start_x = -30
end_x = 30
y_scale = 600 / 900

def match_coordinate_to_screen(x):
    return x * 10

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    screen.fill((0, 0, 0))

    current = start_x

    prev_x = None
    prev_y = None

    while current <= end_x:
        x = current
        y = f(x) * y_scale


        screen_x = match_coordinate_to_screen(x + 30)
        screen_y = int(h - y)
        print(screen_x, screen_y)
        
        if prev_x and prev_y:
            pygame.draw.line(screen, (255, 255, 255), (screen_x, screen_y), (prev_x, prev_y))

        screen.set_at((screen_x, screen_y), (255, 255, 255))
        current += 1
        
        prev_x = screen_x
        prev_y = screen_y

    pygame.display.flip()

pygame.quit()