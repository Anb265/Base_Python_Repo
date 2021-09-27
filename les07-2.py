from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def tissue_consumption(self):
        pass

class Coat(Clothes):
    def __init__(self, name, V):
        Clothes.__init__(self, name)
        self.V = V

    @property
    def tissue_consumption(self):
        consump = (self.V/6.5 + 0.5)
        self.consump = consump
        return (f'Расход ткани на пальто: {consump:.2f}')


class Suit(Clothes):
    def __init__(self, name, H):
        Clothes.__init__(self, name)
        self.H = H

    @property
    def tissue_consumption(self):
        consump = (2 * self.H + 0.3)
        self.consump = consump
        return (f'Расход ткани на пальто: {consump:.2f}')


coat = Coat('пальто', 10)
suit = Suit('костюм', 10)

print(coat.tissue_consumption)
print(suit.tissue_consumption)
print(f'Суммарный расход ткани: {coat.consump + suit.consump:.2f}')

