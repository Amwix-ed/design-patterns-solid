<?php
class Bird {}

interface Flyable {
    public function fly();
}

class Sparrow extends Bird implements Flyable {
    public function fly() {
        echo "Vuelo correctamente";
    }
}

class Penguin extends Bird {
}
?>