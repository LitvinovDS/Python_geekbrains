class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self):
        return 'Масса асфальта = {} кг'.format(self._width * self._length * 25 * 5)


test_road = Road(100, 50)
print(test_road.mass())


