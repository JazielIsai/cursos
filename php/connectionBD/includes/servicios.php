<?php

require 'functions.php';

$servicios = obtenerServicios();

echo json_encode($servicios);