<?php include 'includes/header.php';

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

foreach($products as $producto) { ?>
    
    <li>
        <p> Product: <?php  echo $producto['nombre'];  ?> </p>
        <p> Precio: <?php echo "$ " .$producto['precio']; ?> </p>
        <p> <?php echo ($producto['disponible']) ? 'Disponible' : 'No disponible'; ?> </p>
    </li>

    <?php

}



include 'includes/footer.php'; ?>