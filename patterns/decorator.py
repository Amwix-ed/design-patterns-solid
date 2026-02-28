from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass

class SimpleCoffee(Coffee):
    def cost(self):
        return 5

class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1

if __name__ == "__main__":
    coffee = SugarDecorator(MilkDecorator(SimpleCoffee()))
    print("Costo total:", coffee.cost())
