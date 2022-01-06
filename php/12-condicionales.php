<?php include 'includes/header.php';

$autenticado = true;
$admin = true;

if($autenticado || $admin) {
    echo 'usuario autenticado correctamente';
} else {
    echo 'usuario no existe o verifique nuevamente';
}

echo '<br />';

if($autenticado && $admin) {
    echo 'usuario autenticado ';
} else {
    echo 'usuario no existe';
}

$cliente = [
    'nombre' => 'Pancho',
    'saldo' => 200,
    'informacion' => [
        'tipo' => 'Oro'
    ]
];

echo '<br>';

//if anidados
if(!empty($cliente)) {
    echo 'Hay datos del usuario';
    if($cliente['saldo'] > 0) {
        echo 'cuenta con saldo disponible';
    } else {
        echo 'no tiene saldo disponible';
    }
} else {
    echo 'no hay datos del cliente';
}

echo '<br>';

//else if

if($cliente['saldo'] == 200){
    echo 'Client esta en su limite de saldo';
} else if($cliente['saldo'] <= 100) {
    echo 'el cliente esta debajo de su limite de gastos del dia';
} else {
    echo 'no tiene saldo';
}

echo '<br>';

//switch

$tecnologia = 'JavaScript';

switch ($tecnologia) {
    case 'PHP':
        echo 'PHP lenguaje aprendiendo';
        break;
    case 'JavaScript':
        echo 'El lenguaje de la web';
        break;
    case 'CSS':
        echo 'Lenguaje marcado';
        break;   
    default:
        echo 'proceso de aprendizaje';
        break;
}

include 'includes/footer.php'; ?>