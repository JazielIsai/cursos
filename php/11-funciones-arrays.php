<?php include 'includes/header.php';

// in_array - buscar elementos de un arreglo, verifica si un elemento existe y regresa un boleano
$carrito = ['tablet', 'mobile', 'computadora', 'tele'];

var_dump (in_array('tablet', $carrito));
echo '<br>';
var_dump(in_array('audifonos', $carrito));


//Ordenar elementos de un arreglo 
$numero = array(1,4,7,8,5,2,4);

//Sort los ordena de menor a mayor 
sort($numero);
echo '<pre>';
var_dump($numero);
echo '</pre>';

//rsort los ordena de mayor a menor
rsort($numero);
echo '<pre>';
var_dump($numero);
echo '</pre>';

//Ordenar arreglo asosiatico
$cliente = [
    'saldo' => 2500,
    'nombre' => 'pancho',
    'edad' => 32,
    'tipo' => 'oro'

];

//asort - ordenara el arreglo asosiativo por valores (orden alfabetico)
asort($cliente);

echo '<pre>';
var_dump($cliente);
echo '</pre>';

echo '<br>';

//arsort ordena por valores empezando desde la z primero despues numeros
arsort($cliente); 
echo '<pre>';
var_dump($cliente);
echo '</pre>';

echo '<br>';
//ksort - ordena de manera alfabetica por llaves
ksort($cliente);

echo '<pre>';
var_dump($cliente);
echo '</pre>';

//krsort ordena por llaves de manera alfabetica de la z - a
krsort($cliente); 
echo '<pre>';
var_dump($cliente);
echo '</pre>';

include 'includes/footer.php'; ?>