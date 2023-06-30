from abc import ABC, abstractmethod


class Clothing(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothing):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def fabric_consumption(self):
        return self.size / 6.5 + 0.5


class Suit(Clothing):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def fabric_consumption(self):
        return 2 * self.height + 0.3


# Пример использования
coat = Coat("Пальто", 50)
suit = Suit("Костюм", 180)

print(f"Расход ткани на {coat.name}: {coat.fabric_consumption} метров")
print(f"Расход ткани на {suit.name}: {suit.fabric_consumption} метров")

total_fabric_consumption = coat.fabric_consumption + suit.fabric_consumption
print(f"Общий расход ткани: {total_fabric_consumption} метров")
