<?php
interface Workable {
    public function work();
}

interface Eatable {
    public function eat();
}

class Human implements Workable, Eatable {
    public function work() {
        echo "Trabajando";
    }

    public function eat() {
        echo "Comiendo";
    }
}

class Robot implements Workable {
    public function work() {
        echo "Trabajando";
    }
}
?>