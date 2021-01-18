class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Start rendering'


class Pen(Stationery):
    def draw(self):
        return f'{self.title} start rendering'


class Pencil(Stationery):
    def draw(self):
        return f'{self.title} start rendering'


class Handle(Stationery):
    def draw(self):
        return f'{self.title} start rendering'


pen = Pen('Black pen')
pencil = Pencil('Yellow pencil')
handle = Handle('Red handle')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
