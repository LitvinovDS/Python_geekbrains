class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print('Ручка пишет.')


class Pencil(Stationery):
    def draw(self):
        print('Карандаш пишет.')


class Handle(Stationery):
    def draw(self):
        print('Маркер пишет.')


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
pen.draw()
pencil.draw()
handle.draw()
