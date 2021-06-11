class Tree:
    def __init__(self, approx_age, variety, area, x, y, id=None):
        self.approx_age = approx_age
        self.variety = variety
        self.area = area
        self.x = x
        self.y = y
        self.id = id



    def get_location(self):
        a, b = self.area[:2], self.area[2:4]
        location = f"{a}{self.x}{b}{self.y}"
        return location

