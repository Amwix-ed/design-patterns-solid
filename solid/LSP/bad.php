<?php
class Bird {
    public function fly() {
        echo "Estoy volando";
    }
}

class Penguin extends Bird {
    public function fly() {
        throw new Exception("Los pingüinos no vuelan");
    }
}
?>