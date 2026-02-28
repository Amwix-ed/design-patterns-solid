from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def calculate(self, price):
        pass

class StudentDiscount(Discount):
    def calculate(self, price):
        return price * 0.8

class VipDiscount(Discount):
    def calculate(self, price):
        return price * 0.7

if __name__ == "__main__":
    print(StudentDiscount().calculate(100))
