<?php include 'includes/header.php';

//Arreglos indexados

//Una forma de declararlos
$carrito = ['Tablet', 'Television', 'Computadora'];

//Util para ver los contenidos de un array
echo '<pre>';
var_dump($carrito);
echo '</pre>';

//Acceder elementos de un array
echo $carrito[1];

//opcion 1 de agregar un elemento nuevo al array
$carrito[3] = 'Nuevo producto...';

//Util para ver los contenidos de un array
echo '<pre>';
var_dump($carrito);
echo '</pre>';



//Add new element to end.
array_push($carrito, 'Audifonos');

//Add new element to start 
array_unshift($carrito, 'SmartWath');


echo '<pre>';
var_dump($carrito);
echo '</pre>';



echo 'Otra forma de crear arreglos indexados';

//Otra forma de declarar arreglos indexados es:
$carrito2 = array('Cliente 1', 'Cliente 2', 'Cliente 3'); 

echo '<pre>';
var_dump($carrito2);
echo '</pre>';

echo $carrito2[2];



include 'includes/footer.php'; ?>