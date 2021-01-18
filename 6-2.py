class Road:
    def __init__(self, road_length, road_width):
        self._length = road_length
        self._width = road_width

    def mass(self):
        print(self._length * self._width * 25 * 5)


my_road = Road(20, 5)
my_road.mass()
