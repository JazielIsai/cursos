class Persona{
    constructor (nombre, apellidos, edad){

    }
    Nombre(){

    }
    Apellido(){

    }
    Edad(){

    }
}

//Extends sirve para heredar los metodos y atributos de la super clase
class cliente extends Persona{ 
//con el (super) llamamos al contructor de la clase heredada
constructor(nombre){
    super("Person", apellidos,5)
}
}