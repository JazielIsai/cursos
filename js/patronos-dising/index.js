class MiClase {
    constructor(p1, p2) {
        this.propiedad = p1;
        this.propiedad1 = p2;

    }
    method ( ) {
        //soy un metodo de prototipo
    }
}

const instancia = new MiClase(2, 3);
//console.log(instancia.__proto__); //es para poder ver la clase en forma de prototipo

