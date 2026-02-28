<?php
interface DatabaseInterface {
    public function connect();
}

class MySQLDatabase implements DatabaseInterface {
    public function connect() {
        echo "Conectando MySQL";
    }
}

class PostgreSQLDatabase implements DatabaseInterface {
    public function connect() {
        echo "Conectando PostgreSQL";
    }
}

class UserService {
    private $db;

    public function __construct(DatabaseInterface $db) {
        $this->db = $db;
    }
}
?>