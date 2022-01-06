<?php include 'includes/header.php';

$numero1 = 20;

$numero2 = 30;

$numero3 =30;

$numero4 = '30';

var_dump($numero1 > $numero2);
echo '<br>';

var_dump($numero1 < $numero2);
echo '<br>';

var_dump($numero1 >= $numero2);
echo '<br>';

var_dump($numero1 <= $numero2);
echo'<br>';

var_dump($numero2 == $numero3);
echo '<br>';

var_dump($numero2 == $numero4);
echo '<br>';

var_dump($numero2 === $numero4);
echo '<br>';

//el comparador <=>. Si el numero de la izquierda es menor al de la derecha = -1, si el numero de la izquierda es mayor al de la derecha es = 1, si los dos valores son iguales es = 0. 
//-1 Si Izquierda es menor
var_dump($numero1 <=> $numero2);
echo'<br>';
//1 si el de la izquierda es mayor
var_dump($numero2 <=> $numero1);
echo '<br>';
//0 si ambos son iguales de la
var_dump($numero2 <=> $numero3);



include 'includes/footer.php'; ?> 