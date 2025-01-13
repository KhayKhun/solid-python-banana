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
    c.move(-20,0)
    c.draw()