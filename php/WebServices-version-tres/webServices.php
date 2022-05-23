<?php

    include 'connection.php';

    $pdo = new Connection();

    //Listar registro y consultar registros

    if($_SERVER['REQUEST_METHOD'] == 'GET' ) {

        if( isset($_GET['id_workflow']) ) {
            $sql = $pdo->prepare('SELECT * FROM test_position WHERE idworkflow=:idworkflow');
            $sql->bindValue(':idworkflow', $_GET['idworkflow']);
            $sql->execute();
            $sql->setFetchMode(PDO::FETCH_ASSOC);

            header("HTTP/1.1 200 hay datos");
            echo json_encode($sql->fetchAll());
            exit;

        } else {
            $sql = $pdo->prepare('SELECT * FROM test_position');
            $sql->execute();
            $sql->setFetchMode(PDO::FETCH_ASSOC);
            header('HTTP/1.1 200 hay datos');
            echo json_encode($sql->fetchAll());
            exit;
        }
    }

    header("HTTP/1.1 400 Bad Request");

?>