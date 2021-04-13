from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def calculate(self):
        pass


class Suit(Clothes):

    @property
    def calculate(self):
        return round(2 * self.size + 0.3, 2)


class Coat(Clothes):

    @property
    def calculate(self):
        return round((self.size / 6.5) + 0.5, 2)


my_suit = Suit(200)
my_coat = Coat(100)
print('Suit = ', my_suit.calculate)
print('Coat = ', my_coat.calculate)
print('Suit and coat = ', my_suit.calculate + my_coat.calculate)
