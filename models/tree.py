class Tree:
    def __init__(self, approx_age, tree_type, area, x, y, id=None):
        self.approx_age = approx_age
        self.tree_type = tree_type
        self.area = area
        self.x = x
        self.y = y
        self.id = id



    def get_location(self):
        a, b = self.area[:2], self.area[2:4]
        location = f"{a}{self.x}{b}{self.y}"
        return location

