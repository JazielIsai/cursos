//Async / Await

function descargarNuevosClientes() {

    return new Promise( resolve => {
        console.log('Descargando clientes ... .... espere. ....');

        setTimeout( ()=> {
            resolve ('Los clientes fueron descargados');
        }, 5000);
    });
}

function descargarUltimosPedidos() {

    return new Promise( resolve => {
        console.log('Descargando pedidos ... .... espere. ....');

        setTimeout( ()=> {
            resolve ('Los pedidos fueron descargados');
        }, 5000);
    });
}

async function app () { 
    try{
//        const cliente = await descargarNuevosClientes();
//        const pedidos = await descargarUltimosPedidos();

//        console.log (cliente);
//        console.log (pedidos);

        //promise.all puedes llamar dos funciones asincronas al mismo tiempo
        const resultado = await Promise.all( [descargarNuevosClientes(), descargarUltimosPedidos()] );
        console.log (resultado[0]);
        console.log (resultado[1]);

    } catch(e){

    }
}


 app();

