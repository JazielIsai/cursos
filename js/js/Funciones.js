//toUpperCase(), transforma todos los caracteres de la cadena a sus correspondientes caracteres en mayúsculas:
var mensaje = "Hola";
var mensaje2 = mensaje.toUpperCase(); //Todas en Mayusculas

//toLowerCase(), transforma todos los caracteres de la cadena a sus correspondientes caracteres en minúsculas:

var mensaj3 = "Hola";
var mensaje4 = mensaje.toLowerCase(); //Todas en Minisculas

//charAt(posicion), obtiene el carácter que se encuentra en la posición indicada:

var mensaj5 = "Hola";
var mensaje6 = mensaje.charAt(0);// mensaje = H
mensaje6.charAt(3); // mensaje = a
 
/*
 indexOf(caracter), calcula la posición en la que se encuentra el carácter indicado dentro de la
cadena de texto. Si el carácter se incluye varias veces dentro de la cadena de texto, se devuelve
su primera posición empezando a buscar desde la izquierda. Si la cadena no contiene el carácter,
la función devuelve el valor -1:
 */
var mensaje = "Hola";
var posicion = mensaje.indexOf('a'); // posicion = 3
posicion = mensaje.indexOf('b'); // posicion = -1

//lastIndexOf(caracter), calcula la última posición en la que se encuentra el carácter indicado dentro de la cadena de texto. Si la cadena no contiene el carácter, la función devuelve el valor -1:
var mensaje = "Hola";
var posicion = mensaje.lastIndexOf('a'); // posicion = 3
posicion = mensaje.lastIndexOf('b'); // posicion = -1

//split(separador), convierte una cadena de texto en un array de cadenas de texto. La función parte la cadena de texto determinando sus trozos a partir del carácter separador indicado:
var mensaje = "Hola Mundo, soy una cadena de texto!";
var palabras = mensaje.split(" ");
// palabras = ["Hola", "Mundo,", "soy", "una", "cadena", "de", "texto!"];

//Con esta función se pueden extraer fácilmente las letras que forman una palabra:
var palabra = "Hola";
var letras = palabra.split(""); // letras = ["H", "o", "l", "a"]

//Funciones útiles para arrays

//A continuación se muestran algunas de las funciones más útiles para el manejo de arrays: length, calcula el número de elementos de un array
var vocales = ["a", "e", "i", "o", "u"];
var numeroVocales = vocales.length; // numeroVocales = 5

//concat(), se emplea para concatenar los elementos de varios arrays
var array1 = [1, 2, 3];
array2 = array1.concat(4, 5, 6); //  array2 = [1, 2, 3, 4, 5, 6]
array3 = array1.concat([4, 5, 6]); //array3 = [1, 2, 3, 4, 5, 6]

//join(separador), es la función contraria a split(). Une todos los elementos de un array para formar una cadena de texto. Para unir los elementos se utiliza el carácter separador indicado
var array = ["hola", "mundo"];
var mensaje = array.join(""); // mensaje = "holamundo"
mensaje = array.join(" "); // mensaje = "hola mundo"

//pop(), elimina el último elemento del array y lo devuelve. El array original se modifica y su longitud disminuye en 1 elemento.
var array = [1, 2, 3];
var ultimo = array.pop();
// ahora array = [1, 2], ultimo = 3

//push(), añade un elemento al final del array. El array original se modifica y aumenta su longitud en 1 elemento. (También es posible añadir más de un elemento a la vez)
var array = [1, 2, 3];
array.push(4);
// ahora array = [1, 2, 3, 4]

//shift(), elimina el primer elemento del array y lo devuelve. El array original se ve modificado y su longitud disminuida en 1 elemento.
var array = [1, 2, 3];
var primero = array.shift();
// ahora array = [2, 3], primero = 1

//unshift(), añade un elemento al principio del array. El array original se modifica y aumenta su longitud en 1 elemento. (También es posible añadir más de un elemento a la vez)
var array = [1, 2, 3];
array.unshift(0);
// ahora array = [0, 1, 2, 3]

//reverse(), modifica un array colocando sus elementos en el orden inverso a su posición original:
var array = [1, 2, 3];
array.reverse();
// ahora array = [3, 2, 1]

//isNaN(), permite proteger a la aplicación de posibles valores numéricos no definidos
var numero1 = 0;
var numero2 = 0;
if(isNaN(numero1/numero2)) {
    alert("La división no está definida para los números indicados");
}
else {
    alert("La división es igual a => " + numero1/numero2);
}

