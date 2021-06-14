class Tree:
    def __init__(self, approx_age, variety, area, x, y, notes, id=None):
        self.approx_age = approx_age
        self.variety = variety
        self.area = area
        self.x = x
        self.y = y
        self.notes = notes
        self.id = id
        

    def get_location(self):
        a, b = self.area[:2], self.area[2:4]
        location = f"{a}{self.x}{b}{self.y}"
        return location

    def get_css_grid_location(self, key):
        grid_translator = {"0002":1, "0102":2, "0202":3, "0001":4, "0101":5, "0201":6, "0000":7, "0100":8, "0200":9}
        return grid_translator[key]

    def get_css_flex(self, key):
        flex_translator = {"0002":"justify-content: flex-start; align-items: flex-start;", "0102":"justify-content: center; align-items: flex-start;", "0202":"justify-content: flex-end; align-items: flex-start;", "0001":"justify-content: flex-start; align-items: center;", "0101":"justify-content: center; align-items: center;", "0201":"justify-content: flex-end; align-items: center;", "0000":"justify-content: flex-start; align-items: flex-end;", "0100":"justify-content: center; align-items: flex-end", "0200":"justify-content: flex-end; align-items: flex-end;"}
        return flex_translator[key]

