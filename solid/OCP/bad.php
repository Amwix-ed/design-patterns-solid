<?php
class Payment {
    public function pay($type) {
        if ($type == "paypal") {
            echo "Pago con PayPal";
        }
        if ($type == "credit") {
            echo "Pago con tarjeta";
        }
    }
}
?>