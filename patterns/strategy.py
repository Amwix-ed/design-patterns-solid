from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

class AddStrategy(Strategy):
    def execute(self, a, b):
        return a + b

class SubtractStrategy(Strategy):
    def execute(self, a, b):
        return a - b

class MultiplyStrategy(Strategy):
    def execute(self, a, b):
        return a * b

class Context:
    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self.strategy = strategy

    def execute(self, a, b):
        return self.strategy.execute(a, b)

if __name__ == "__main__":
    context = Context(AddStrategy())
    print(context.execute(10, 5))
    context.set_strategy(MultiplyStrategy())
    print(context.execute(10, 5))
