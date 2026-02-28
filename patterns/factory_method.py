from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass

class Truck(Transport):
    def deliver(self):
        return "Entrega por tierra en camión"

class Ship(Transport):
    def deliver(self):
        return "Entrega por mar en barco"

class Logistics(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
        pass

    def plan_delivery(self):
        transport = self.create_transport()
        print(transport.deliver())

class RoadLogistics(Logistics):
    def create_transport(self):
        return Truck()

class SeaLogistics(Logistics):
    def create_transport(self):
        return Ship()

if __name__ == "__main__":
    RoadLogistics().plan_delivery()
    SeaLogistics().plan_delivery()
