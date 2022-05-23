<?php
$user = "root";
$pass = "";
$host = "localhost";
$name_bd = "prueba";
$port = 3307;


$db = mysqli_connect($host, $user, $pass, $name_bd, $port);


if(!$db){
    echo "No se ha podido conectar con el servidor";
    exit;
} else {
    echo 'conexion establecida';
}


