<?php
    class Conectar {
        protected $dbh;
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

        protected function Conection() {
            try {
                $connection = "mysql:host=". $this->host.";dbname=". $this->db . ";charset=". $this->charset . ";port=" . $this->port;
                //$connection = $this->dbh = new PDO("mysql:local=localhost;dbname=prueba", "root", "");
                $options = [
                    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
                    PDO::ATTR_EMULATE_PREPARES => false
                ];

                //$pdo = new PDO($connection, $this->user, $this->password, $options);
                $pdo = new PDO($connection, $this->user, $this->password);
                return $pdo;


            } catch (Exception $err) {
                print "Error DB!: " . $err->getMessage() . "<br/>";
                die();
            }
        }

        public  function set_position() {
            return $this->dbh->query('SET_POSITION "utf8mb4"');
        }


    }