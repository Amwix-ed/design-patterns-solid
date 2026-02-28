<?php
class UserRepository {
    private $connection;

    public function __construct($connection) {
        $this->connection = $connection;
    }

    public function save($name, $email) {
        $stmt = $this->connection->prepare(
            "INSERT INTO users (name, email) VALUES (?, ?)"
        );
        $stmt->bind_param("ss", $name, $email);
        $stmt->execute();
    }
}

class EmailService {
    public function send($email) {
        mail($email, "Bienvenido", "Gracias por registrarte");
    }
}

class ReportService {
    public function generate() {
        echo "Reporte generado";
    }
}
?>