from abc import ABC, abstractmethod

class CoffeeBuilder(ABC):
    @property
    @abstractmethod
    def coffee(self):
        pass

    @abstractmethod
    def add_water(self, water: int) -> None:
        pass

    @abstractmethod
    def add_coffee_beans(self, beans: int) -> None:
        pass

    @abstractmethod
    def add_milk(self, milk: int) -> None:
        pass

    @abstractmethod
    def add_sugar(self, sugar: int) -> None:
        pass

class EspressoBuilder(CoffeeBuilder):
    def __init__(self):
        self.__coffee = {}

    @property
    def coffee(self):
        return self.__coffee

    def add_water(self, water: int) -> None:
        self.__coffee["water"] = water

    def add_coffee_beans(self, beans: int) -> None:
        self.__coffee["beans"] = beans

    def add_milk(self, milk: int) -> None:
        self.__coffee["milk"] = milk

    def add_sugar(self, sugar: int) -> None:
        self.__coffee["sugar"] = sugar

class CoffeeDirector:
    def __init__(self, builder: CoffeeBuilder):
        self.builder = builder

    def construct_espresso(self) -> None:
        self.builder.add_water(50)
        self.builder.add_coffee_beans(20)
        self.builder.add_milk(30)
        self.builder.add_sugar(15)

    def construct_latte(self) -> None:
        self.builder.add_water(100)
        self.builder.add_coffee_beans(20)
        self.builder.add_milk(60)
        self.builder.add_sugar(20)

def main():
    espresso_builder = EspressoBuilder()
    latte_builder = EspressoBuilder()

    director = CoffeeDirector(espresso_builder)
    director.construct_espresso()
    print("Эспрессо:", espresso_builder.coffee)

    director = CoffeeDirector(latte_builder)
    director.construct_latte()
    print("Латте:", latte_builder.coffee)

if __name__ == "__main__":
    main()
