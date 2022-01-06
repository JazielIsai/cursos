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

var libros = new inventario("Libro");
libros.add("Angualar.js",3);
libros.add("JavaScript", 10);
libros.add("Node js", 5);

libros.cantidad("Angular.js");
libros.cantidad("JavaScript");
libros.borrar("Angular.js");
libros.cantidad("JavaScript");




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