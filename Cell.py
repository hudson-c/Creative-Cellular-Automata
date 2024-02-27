class Cell:
    def __init__(self, r=0, g=0, b=0):
        self.r = r
        self.g = g
        self.b = b
        self.is_dead = not (r and g and b)

    def __str__(self):
        return f"({self.r}, {self.g}, {self.b})"

    def colour(self):
        return (self.r, self.g, self.b)
