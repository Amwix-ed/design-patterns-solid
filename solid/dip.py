from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        print("Conectando a MySQL")

class Application:
    def __init__(self, database: Database):
        self.database = database

    def start(self):
        self.database.connect()

if __name__ == "__main__":
    app = Application(MySQLDatabase())
    app.start()
