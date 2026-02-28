class Worker:
    def work(self):
        pass

class Human:
    def eat(self):
        pass

class Employee(Worker, Human):
    pass

class Robot(Worker):
    pass
