<?php
class MySQLDatabase {
    public function connect() {}
}

class UserService {
    private $db;

    public function __construct() {
        $this->db = new MySQLDatabase();
    }
}
?>