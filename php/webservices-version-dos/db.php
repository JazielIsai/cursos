<?php

    class DB {
        private $host;
        private $db;
        private $user;
        private $password;
        private $charset;
        private $port;

        public function __construct(){
            $this->host = "localhost";
            $this->db = "prueba";
            $this->user = "root";
            $this->password="1234";
            $this->charset="utf8mb4";
            $this->port=3307;
        }

        function connect() {
            try {
                $connection = "mysql:host=". $this->host.";dbname=". $this->db . ";charset=". $this->charset . ";port=" . $this->port;
                $options = [
                    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
                    PDO::ATTR_EMULATE_PREPARES => false
                ];

                //$pdo = new PDO($connection, $this->user, $this->password, $options);
                $pdo = new PDO($connection, $this->user, $this->password);
                return $pdo;

            }catch(PDOException $e){
                print_r('Error connection: ' . $e->getMessage());
            }

        }
    }
?>