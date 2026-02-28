class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        pass

class EmailObserver(Observer):
    def update(self, message):
        print(f"Email recibido: {message}")

class SMSObserver(Observer):
    def update(self, message):
        print(f"SMS recibido: {message}")

if __name__ == "__main__":
    subject = Subject()
    subject.attach(EmailObserver())
    subject.attach(SMSObserver())
    subject.notify("Producto disponible!")
