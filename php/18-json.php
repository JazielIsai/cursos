<?php

include 'includes/header.php';


$products = [
    [
        'nombre' => 'Tablet',
        'precio' => 4500,
        'disponible' => true
    ],
    [
        'nombre' => 'televicion 32"',
        'precio' => 6000,
        'disponible' => true
    ],
    [
        'nombre' => 'Monitor Curvo',
        'precio' => 5000,
        'disponible' => false
    ]
];


echo '<pre>';
var_dump($products);


//Para que esto lo lea js se necesita convertir primeramente
$json = json_encode($products, JSON_UNESCAPED_UNICODE);//json_encode convierte un arreglo en un string
//JSON_UNESCAPED_UNICODE CONVIERTE LOS ASENTOS O HACE QUE SE PUEDAN LEER

//json_decode se usa para convertir un string a un arreglo que pueda leer php
$json_array = json_decode($json);

var_dump($json);

var_dump($json_array);


echo '</pre>';



include 'includes/footer.php'; ?>