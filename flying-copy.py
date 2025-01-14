import pygame
import sys
import random


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


# pygame init
pygame.init()
BG_COLOR = (30, 30, 30)
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Flying circle")
clock = pygame.time.Clock()

running = True

# circles init
circles = [Circle(
    color=(0, 200, 0),
    radius=random.randint(5, 10),  # ha
    x=random.randint(0, WINDOW_WIDTH),
    y=random.randint(0, WINDOW_HEIGHT),
    vx=random.randint(3, 20),
    vy=random.randint(3, 20),
    ) for _ in range(10)]

# game run
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    screen.fill(BG_COLOR)

    for c in circles:
        # print('radius',c.radius)
        # print('vx',c.vx)
        # print('vy',c.vy)
        # print('x',c.x)
        # print('y',c.y)
        c.move_and_draw()

    pygame.display.flip()
    clock.tick(30)

# Clean up
pygame.quit()
sys.exit()
