class inventario
{
    constructor(nombre)
    {
        this.nombre=nombre;
        this.articulos = [];
    }

    add (nombre, cantidad)
    {
        this.articulos[nombre] = cantidad;
    }

    borrar (nombre)
    {
        delete this.articulos[nombre];
    }

    cantidad (nombre)
    {
        return this.articulos[nombre];
    }

    getNombre ()
    {
        return this.nombre;
    }
}

var book = new inventario("Libro");
book.add("Angualar.js",3);
book.add("JavaScript", 10);
book.add("Node js", 5);

book.cantidad("Angular.js");
book.cantidad("JavaScript");
book.borrar("Angular.js");
book.cantidad("JavaScript");




//Implementacion de herencia
class Vehiculo
{
    constructor(tipo, nombre, ruedas)
    {
        this.tipo = tipo;
        this.nombre = nombre;
        this.ruedas = ruedas;
    }

    getRuedas()
    {
        return this.ruedas;
    }

    arrancar()
    {
        console.log('Arrancando el ${(this.nombre)}');
    }

    aparcar()
    {
        console.log('Aparcando el ${(this.nombre)}');
    }
}

class Coche extends Vehiculo
{
    constructor (nombre)
    {
        super("Coche", nombre,4)
    }
}

let fordFocus = new Coche("FordFocus");
fordFocus.getRuedas();
fordFocus.arrancar();