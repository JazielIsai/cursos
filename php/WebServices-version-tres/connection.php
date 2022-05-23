<?php

    class Connection extends PDO {
        private $localhost = 'localhost';
        private $user = 'root';
        private $nameBD = 'prueba';
        private $password = '';
        private $port = 3307;

        public function __construct()
        {
            try {
                parent::__construct('mysql:host=' . $this->localhost . '; dbname=' . $this->nameBD . ';port=' . $this->port . ';charset=utf8', $this->user, $this->password, array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION)  );
                echo 'Connection successes';

            } catch (PDOException $e) {
                echo 'Error: ' . $e->getMessage();
                exit();
            }
        }
    }

?>