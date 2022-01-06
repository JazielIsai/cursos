<?php
declare(strict_types=1);

include 'includes/header.php';

                                                //Retrona string
function usuarioAutenticado(bool $autenticado) : string {
    if($autenticado){
        return 'El usuario ha sido autenticado.';
    } else {
        return null;
    }
}
                                                //Es opcional el retorno de string
function usuarioAutenticado1(bool $autenticado) : ?string {
    if($autenticado){
        return 'El usuario ha sido autenticado.';
    } else {
        return null;
    }
}


$usuario = usuarioAutenticado1(true);

echo $usuario;

include 'includes/footer.php'; ?>