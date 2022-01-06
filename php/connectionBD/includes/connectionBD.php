<?php 

$db = mysqli_connect('localhost', 'root', '1234', 'appsalon');


if(!$db){
    echo 'Error en la conexion';
    exit;
} else {
    echo 'conexion establecida';
}

?>
