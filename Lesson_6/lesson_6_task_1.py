from time import sleep


class TrafficLight:
    def __init__(self):
        self.__color = [('Red', 7), ('Yellow', 2), ('Green', 4)]

    def run(self):
        i = 0
        while True:
            print(self.__color[i][0], 'Время ожидания {} сек.'.format(self.__color[i][1]))
            sleep(1)
            for n in range(self.__color[i][1] - 1):
                print((int(self.__color[i][1]) - n - 1), '...')
                sleep(1)
            if i >= 2:
                i = 0
            else:
                i += 1


light = TrafficLight()
light.run()