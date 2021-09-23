class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Вы выбрали {self.title} для рисования.')


class Pencil(Stationery):
    def draw(self):
        print(f'Вы выбрали {self.title} для рисования.')

class Handle(Stationery):
    def draw(self):
        print(f'Вы выбрали {self.title} для рисования.')


pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')
stat = Stationery('что-то для рисования')

stat.draw()
pen.draw()
pencil.draw()
handle.draw()
