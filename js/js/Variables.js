/* // Var, Let, const
//ECMAScript6

var nombre = "Jose Montoya";
Console.log(nombre);

nombre = "Juan Matatias";
Console.log(nombre);

//Iniciar una variable
var numero;
console.log(numero);
numero = 12;
Console.log(numero);

//Letras, numeros, _, $
//No se puede iniciar con numeros

//Recomendadciones para crear variables
var primerNombre = "Juan";//Escritura tipo camello (Camel case)
var primer_nombre = "Pedro";//Tipo guion bajo (underscore)
var PrimerNombre ="Jorge";//Tipo Pascal (pascal case) */

let nombre;
nombre = "Jose Montoña";
Console.log(nombre);

nombre = "Juan Hernandez";
console.log(nombre);

//CONST

const nombre2 = "Juan";
console.log(nombre2);
//No se puede reasignar
//nombre2 = "Angelica";
//No se puede declarar una constante sin asignarle un valor
//const apellido;


//Scope o el alcance de la variable
//Para la creacion de ciclos es mejor el let que el var
for(let i = 0; i <= 5; i++)
{
    console.log(i);
}

//Const para objetos
const persona = {
    nombre: 'Jose',
    apellido: 'Montoya' 
}

persona.nombre = 'Josue';

const numeros = [1,2,3,4,5,6];
numeros.push(7); // .push permite agregar nuevos valores al arreglo
console.log(numeros);