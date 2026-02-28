import math

class RoundHole:
    def __init__(self, radius):
        self.radius = radius

    def fits(self, peg):
        return self.radius >= peg.get_radius()

class RoundPeg:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

class SquarePeg:
    def __init__(self, width):
        self.width = width

    def get_width(self):
        return self.width

class SquarePegAdapter(RoundPeg):
    def __init__(self, square_peg: SquarePeg):
        self.square_peg = square_peg

    def get_radius(self):
        return self.square_peg.get_width() * math.sqrt(2) / 2

if __name__ == "__main__":
    hole = RoundHole(5)
    adapter = SquarePegAdapter(SquarePeg(5))
    print("¿Encaja?", hole.fits(adapter))
