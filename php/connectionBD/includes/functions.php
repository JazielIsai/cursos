<?php 

function obtenerServicios() : array {
    try {

        //Importar una conexion de
        require 'connectionBD.php';
        //var_dump($db);

        ///Escribir un codigo sql
        $query = 'select * from test_position';

        $consulta = mysqli_query($db, $query);

        //arreglo vacio
        $servicios = [];

        $i = 0;

        //obtener los resultados

        while($row = mysqli_fetch_assoc($consulta)){
            $servicios[$i]['id_workflow'] = $row['id_workflow'];
            $servicios[$i]['x_axis'] = $row['x_axis'];
            $servicios[$i]['y_axis'] = $row['y_axis'];

            $i++;
        }   

        echo '<pre>';
        var_dump(json_encode($servicios));
        echo '</pre>';

        return $servicios;
        //echo '<pre>';
        //var_dump(mysqli_fetch_assoc($consulta));
        //var_dump(mysqli_fetch_all($consulta)); //trae todos los resultados
        //var_dump(mysqli_fetch_array($consulta)); //de manera de arreglo trae los valores
        //var_dump(mysqli_fetch_assoc($consulta)); //trae valores como un arreglo asosiativo
        //echo '</pre>';



    } catch (\Throwable $e){
        //throw $e;
        var_dump($e);
    }
}

obtenerServicios();

