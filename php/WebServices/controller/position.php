<?php
    //require_once('../config/Connection.php');
    //require_once('../models/Position.php');
    include_once '../config/Connection.php';
    include_once '../models/Position.php';


    $position = new Position();

    if ($_GET["op"] == "GetAll") {
        $positions = array();
        $positions['items'] = array();

        $res = $position->getPosition();

        if ($res->rowCount()) {
            while ($row = $res->fetch(PDO::FETCH_ASSOC)) {

                $item = array(
                    "id_workflow" => $row['id_workflow'],
                    "x_axis" => $row['x_axis'],
                    "y_axis" => $row['y_axis'],
                );
                array_push($positions["items"], $item);
            }

            echo json_encode($positions);
        } else {
            echo json_encode(array('mensaje' => 'No hay elementos'));
        }
    }

?>