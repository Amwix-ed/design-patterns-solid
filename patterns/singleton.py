class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creando nueva instancia de Database...")
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    def query(self, sql):
        print(f"Ejecutando consulta: {sql}")


if __name__ == "__main__":
    db1 = Database()
    db2 = Database()
    db1.query("SELECT * FROM users")
    print("¿Son la misma instancia?", db1 is db2)
