from abc import ABC, abstractmethod


class AbstractClothes(ABC):
    @abstractmethod
    def add_coat(self, v):
        pass

    @abstractmethod
    def add_suit(self, h):
        pass

    @abstractmethod
    def common_amount_of_fabric(self):
        pass


class Coat:
    def __init__(self, v):
        self.volume = v

    @property
    def coat_amount_of_fabric(self):
        return self.volume / 6.5 + 0.5


class Suit:
    def __init__(self, h):
        self.height = h

    @property
    def suit_amount_of_fabric(self):
        return 2 * self.height + 0.3


class Clothes(AbstractClothes):
    def __init__(self, title):
        self.title = title
        self.coat = []
        self.suit = []

    def add_coat(self, v):
        self.coat.append(Coat(v))

    def add_suit(self, h):
        self.suit.append(Suit(h))

    @property
    def common_amount_of_fabric(self):
        common_amount_of_fabric = 0
        for el in self.coat:
            common_amount_of_fabric += el.coat_amount_of_fabric
        for el in self.suit:
            common_amount_of_fabric += el.suit_amount_of_fabric
        return f'Общее необходимое количество ткани: {common_amount_of_fabric}'


cloth = Clothes('Мужская одежда')
cloth.add_coat(6.5)
cloth.add_coat(6.5)
cloth.add_suit(3)
print(cloth.title)
print(cloth.common_amount_of_fabric)
