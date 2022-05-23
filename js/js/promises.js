
//En los promises existen 3 valores posibles 
//pending : no se ha cumplido pero tampoco se ha rechazado
// Fulfilled : Ya se cumplio
// Rejected : Se ha rechazado o no se pudo cumplir 


const usuarioAutenticado = new Promise ( (resolve, reject) => {
    const auth = false;

    if(auth) {
        //Resolve se ejecuta cundo la promesa se cumple
        resolve('El usuario ha ingresado correctamente'); 
    } else {
        //reject se ejecuta cuando la promesa no se cumple
        reject('No se puedo iniciar sesion');
    }
});

usuarioAutenticado
    .then( res => document.querySelector('p').textContent = res) //El then se ejecuta y trae el valor que en el resolve ha sido ejecutado
    .catch( err => document.querySelector('p').textContent = err) //el catch se ejecuta atrapando el error que trae el reject
