<?php
interface PaymentMethod {
    public function pay();
}

class Paypal implements PaymentMethod {
    public function pay() {
        echo "Pago con PayPal";
    }
}

class CreditCard implements PaymentMethod {
    public function pay() {
        echo "Pago con tarjeta";
    }
}

class Payment {
    private $method;

    public function __construct(PaymentMethod $method) {
        $this->method = $method;
    }

    public function process() {
        $this->method->pay();
    }
}
?>