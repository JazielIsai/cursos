<?php include 'includes/header.php';

//Arreglos asociativos 
$cliente = [
    'nombre' => 'Jaziel',
    'saldo' => 200,
    'informacion' => [
        'tipo' => 'premium',
        'cuenta'=>  2131432425435,
        'disponible' => 1000
    ]
];

echo '<pre>';
var_dump($cliente);
echo '</pre>';

//Para acceder a una sola propiedad es
//echo $cliente['nombre'];
//echo '<br>';
//echo $cliente['informacion']['tipo'];

//Agregar una propiedad que no existe
$cliente['codigo'] = 00213234;



echo '<pre>';
var_dump($cliente);
echo '</pre>';



include 'includes/footer.php'; ?>