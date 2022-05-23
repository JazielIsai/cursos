<?php include 'includes/header.php';

//Arreglos indexados
$clientes = [];
$clientes = array();

$clientes3 = array('pedro','juan','agustin');

//Arreglo asosiativo
$client = [
    'nombre' => 'Jaziel',
    'edad' => 21
];

//Empty - es uttil para saber si un arreglo esta vacio o no lo esta vacio
var_dump(empty($clientes));
echo '<br>';
var_dump(empty($clientes3));
echo '<br>';

//Isset - revisa si un arreglo esta creada o si una propiedad esta definida

var_dump(isset($client2));
echo'<br>';
var_dump(isset($clientes));
echo '<br>';
var_dump(isset($clientes3));
echo '<br>';

//Isset - revisa si una propiedad esta definida 
var_dump(isset($client['nombre']));
echo '<br>';
var_dump(isset($client['apellidos']));


include 'includes/footer.php'; ?>