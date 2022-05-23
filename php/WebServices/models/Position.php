<?php
    class Position extends Conectar {

        function getPosition(){
            $query = $this->Conection()->query('select * from test_position;');
            return $query;
        }
    }
?>