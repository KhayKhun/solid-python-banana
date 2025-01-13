SCREEN_W = 200
SCREEN_H = 200


class Circle:
    def __init__(self, radius, x, y):
        self.radius = radius
        self.x = x
        self.y = y

    def draw(self):
        print(f"x:{self.x}, y:{self.y}")

    def move(self, dx = 0, dy = 0):
        self.x += dx
        self.y += dy




if __name__ == "__main__":
    c = Circle(10,100,100)            
    c.draw()

    while c.x < SCREEN_W:
        c.move(10)
        c.draw()