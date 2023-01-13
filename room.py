class Room:
    def __init__(self, name, north, south, east, west) -> str:
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west

    def __str__(self):
        return f'{self.name}'
