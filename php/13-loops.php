<?php include 'includes/header.php';


//While - se ejecuta hasta que la condicion sea falsa

//$i = 0;

//while($i < 10){
//    echo $i . "<br />";
//    $i++;
//}
/*
//otra sintaxis de while
$i = 0;
while ($i < 10) :
    echo $i . "<br />";
endwhile;

echo 'Nuevo conteo <br />';

$i = 0;

//do while
do {
    echo $i ."<br />";

    $i++;
} while ($i < 10);

echo 'Nuevo conteo <br />';

//for loop

for ($i = 0; $i < 10; $i++) {
    echo $i ."<br />";
}
*/
/**
 * 3 imprimir Fizz
 * 5 imprimir Buzz
 * 3 y 5 imprimir FIZZ BUZZ
 */
echo '<br />';
/*
for ($i = 0; $i < 50; $i++) {
    if ($i % 3 == 0 && $i % 5 == 0) {
        echo $i ."... Es Fizz Buzz <br />";
    } else if ($i % 3 == 0) {
        echo $i .'... Es Buzz <br />';
    } elseif ($i % 3 == 0) {
        echo $i ."... Es Fizz <br />";
    }
}
*/
//otra sintaxis de for
//for ($i = 0; $i < 10; $i++):

//endfor;

//For Each
$clientes = array('pedro', 'juan', 'Karen');

foreach ($clientes as $client) {
    echo $client ."<br />";
}


//foreach($clientes as $client):
//    echo $client ."<br />";
//endforeach;

echo '<br />';
//la funcion de count sirve para conocer el tama;o del arreglo
echo count($clientes);

echo '<br />';

//la funcion sizeof sirve para conocer el tama;o del arreglo
echo sizeof($clientes);

echo '<br />';

//for each con un arreglo asosiativo
$client = [
    'nombre' => 'jaziel',
    'apellidos' => 'Perez',
    'edad' => 21
];

foreach ($client as $key => $value) {
    echo $key . "--" . $value . '<br />';
}



include 'includes/footer.php';
