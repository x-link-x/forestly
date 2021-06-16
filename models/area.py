class Area:
    def __init__(self, easting, northing, id=None):
        self.easting = easting
        self.northing = northing
        self.id = id
          
    def get_grid_reference(self):
        return f"{self.easting}{self.northing}"