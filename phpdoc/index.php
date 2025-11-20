<?php
class Uczen {
    public $name;
    public $color;

    function set_name($name) {
        $this->name = $name;
    }

    function get_name() {
        return $this->name;
    }
}

$uczen1 = new Uczen();
$uczen1->set_name('Oskar Ciebielski');
echo $uczen1->get_name();
?>
