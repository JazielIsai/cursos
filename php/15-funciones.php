<?php 
declare(strict_types = 1);

include 'includes/header.php';



function sumar(int $num1 = 0, int $num2 = 0){
    echo $num1 + $num2;
}

sumar(2,43);

echo "<br/>";

//Parametro nombrado / named parameters
//sumar(num2: 20, num1: 30);

include 'includes/footer.php'?>