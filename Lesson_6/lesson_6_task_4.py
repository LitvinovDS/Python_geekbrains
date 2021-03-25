class Car:
    def __init__(self, speed, color, name, is_polece):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_polece

    def go(self):
        print(f'Авто {self.name} движется.')

    def stop(self):
        print(f'Авто {self.name} стоит.')

    def turn(self, direction):
        print(f'Автмобиль {self.name} повернул ', direction)

    def show_speed(self):
        print(f'Скорость автомобиля {self.name} составляет', self.speed)


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Превышение скорости!')


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Превышение скорости!')


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


town = TownCar(120, 'White', 'Kia', False)
work = WorkCar(60, 'Yellow', 'Kamaz', False)
sport = SportCar(300, 'Purple', 'Lamborgini', False)
police = PoliceCar(220, 'Black', 'Ford', True)
town.show_speed()
work.show_speed()
sport.go()
police.stop()
sport.turn('налево')
