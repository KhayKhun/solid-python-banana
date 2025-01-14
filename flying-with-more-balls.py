import pygame
import sys
from random import randint
import math


BG_COLOR = (30, 30, 30)
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500


class Circle:
    def __init__(self, color, radius, x, y, vx, vy):
        self.color = color
        self.radius = radius
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.vx
        self.y += self.vy
        # check borders
        if self.x > WINDOW_WIDTH or self.x < 0:
            self.vx = -self.vx

        if self.y > WINDOW_HEIGHT or self.y < 0:
            self.vy = -self.vy

    def move_and_draw(self):
        self.move()
        self.draw(screen)
        self.detect_bounce()

    def detect_bounce(self):
        other_circles = circles.copy()
        other_circles.remove(self)

        for oc in other_circles:

            distance = math.sqrt((oc.x - self.x)**2 + (oc.y - self.y)**2)
            
            if distance <= oc.radius + self.radius:
                # Circles are colliding
                self.vx = -self.vx
                self.vy = -self.vy

# pygame init
pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Flying circle")
clock = pygame.time.Clock()

running = True

# circles init
circles = [Circle(
    color=(randint(0, 255), randint(0, 255), randint(0, 255)),
    radius=randint(50, 70),  # ha
    x=randint(0, WINDOW_WIDTH),
    y=randint(0, WINDOW_HEIGHT),
    vx=randint(3, 20),
    vy=randint(3, 20),
) for _ in range(2)]

circles[0].detect_bounce()


# game run
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    screen.fill(BG_COLOR)

    for c in circles:
        c.move_and_draw()

    pygame.display.flip()
    clock.tick(10)

# Clean up
pygame.quit()
sys.exit()
