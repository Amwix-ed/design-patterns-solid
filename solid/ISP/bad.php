<?php
interface Worker {
    public function work();
    public function eat();
}

class Robot implements Worker {
    public function work() {
        echo "Trabajando";
    }

    public function eat() {
        // Robot no come
    }
}
?>