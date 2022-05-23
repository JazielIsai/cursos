<?php
    include_once 'position.php';

    class ApiPosition {

        function getAll( ) {
            $position = new Position();
            $positions = array();

            $positions['items'] = array();

            $res = $position->getPosition();

            if($res->rowCount()){
                while ($row = $res->fetch(PDO::FETCH_ASSOC)){

                    $item=array(
                        "id_workflow" => $row['id_workflow'],
                        "x_axis" => $row['x_axis'],
                        "y_axis" => $row['y_axis'],
                    );
                    array_push($positions["items"], $item);
                }

                echo json_encode($positions);
            }else{
                echo json_encode(array('mensaje' => 'No hay elementos'));
            }



        }
    }
?>