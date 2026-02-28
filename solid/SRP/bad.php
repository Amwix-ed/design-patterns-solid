<?php
class User {
    public function save($name, $email) {
        $conn = new mysqli("localhost", "root", "", "design_patterns");
        $conn->query("INSERT INTO users (name, email) VALUES ('$name','$email')");
    }

    public function sendEmail($email) {
        mail($email, "Bienvenido", "Gracias por registrarte");
    }

    public function generateReport() {
        echo "Reporte generado";
    }
}
?>