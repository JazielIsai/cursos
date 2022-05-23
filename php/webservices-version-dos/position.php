<?php
    include_once 'db.php';

    class Position extends DB{

        function getPosition(){
            $query = $this->connect()->query('select * from test_position;');
            return $query;
        }
    }
?>