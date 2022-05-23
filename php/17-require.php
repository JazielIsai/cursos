<?php

require 'includes/header.php';

//require es lo mismo que include

//require se usa mas cuando la funcion son criticas, como la conexion a la base de datos

//se usa include cuando se desee incluir otros templates

//require_once verifica si ya se haincluido , si ya ha sido creado no lo ingresa, pero si no ha sido llamada lo ocupa


require 'funciones.php';

$cadena = iniciarAPP();
echo $cadena;

include 'includes/footer.php'; ?>