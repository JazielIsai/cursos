<?php

require 'functions.php';

$services = obtenerServicios();

echo json_encode($services);