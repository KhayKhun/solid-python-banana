import time
SCREEN_W = 100
SCREEN_H = 100
running = True

change_x = 10
change_y = 10


class Circle:
    def __init__(self, radius, x, y):
        self.radius = radius
        self.x = x
        self.y = y

    def draw(self):
        print(f"x:{self.x}, y:{self.y}")

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy


if __name__ == "__main__":
    c = Circle(10, 60, 0)
    c.draw()

    while running:
        if c.x == SCREEN_W:
            change_x = -10
        elif c.x == 0:
            change_x = 10

        if c.y == SCREEN_H:
            change_y = -10
        elif c.y == 0:
            change_y = 10

        c.move(change_x, change_y)
        c.draw()
        time.sleep(0.3)