<?php include 'includes/header.php';


$nombreCliente = "         Jaziel";
// strlen() es un metodo para saber la extencion del string
echo strlen($nombreCliente);

echo '<br>';

//trim() Elimina los espacios en blanco
$texto = trim($nombreCliente);
echo strlen($texto);

echo '<br>';

//Convertir a mayusculas
echo strtoupper($texto);

echo '<br>';

//Convertir a minisculas el texto
echo strtolower($texto);

echo '<br>';

$mail1 = 'bebeyoda@gmail.com';
$mail2 = 'Bebeyoda@gmail.com';

var_dump(strtolower($mail1) === strtolower($mail2));

echo '<br>';

//Remplzar caracterres 
echo str_replace('Jaziel', 'J Isai', $texto);

echo '<br>';

//Revisar si un string existe o no
echo strpos($nombreCliente, 'Jaziel');

echo '<br>';

$tipoCliente = "Premium";


//Formas de concatenar
echo "El cliente es:" .$nombreCliente ." y el tipo del cliente es: " .$tipoCliente;

echo '<br>';

echo "El cliente es: {$nombreCliente} y es: {$tipoCliente}";


include 'includes/footer.php'; ?> 