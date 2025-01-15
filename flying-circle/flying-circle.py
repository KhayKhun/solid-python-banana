# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
SCREEN_W = 1280
SCREEN_H = 720

change_x = 10
change_y = 10

current_x = 500
current_y = 0

pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
clock = pygame.time.Clock()
running = True



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    # RENDER YOUR GAME HERE


    if current_x == SCREEN_W:
        change_x = -10
    elif current_x == 0:
        change_x = 10

    if current_y == SCREEN_H:
        change_y = -10
    elif current_y == 0:
        change_y = 10
    
    current_x += change_x
    current_y += change_y

    pygame.draw.circle(screen, (0,0,0), (current_x, current_y), 20 ,20)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
        