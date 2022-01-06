alert("Hola ¿como estas?"); // manda mensaje al usuario antes de empezar 
console.log("Hola mundo");
console.error("Has cometido un error");
console.warn("Advertencia");
var hasta = "hasta cuando seras un niño";
console.log("has lo que se te dice:", hasta);
hasta=3-2;

if(hasta == 5)
{
    console.log(hasta);    
}
else{
    console.log(3-2); 
}

switch(hasta)
{
    case 1:
        console.log(2);
    break;
}
var cadena = prompt(hasta); // alamcena en una variable otra el contenido de otra variable

var condicion = 0;
while(condicion < 100)
{
    console.log(condicion);
    condicion++;
}  

for(var i = 0; i < 100; i++)
{
    console.log(i);
} 

var dato = false;
do{
console.log("Escribi hasta que se cumpla");
}while(dato);

console.info(dato);

var x=2;
var y=1;
x -= y; // x = x - y;
x *= y; // x= x * y;
x += y; // x = x + y;
x /= y; // x = x / y;
x %= y; // x = x % y;

window.alert("Bienvenido a la web"); // Muestra nuestro mensaje en una ventana
window.confirm("Desea seguir"); //Pregunta al usuario y ofrece dos botones que se traducen en valores booleanos. Aceptar (true) y cancelar o cerrar la ventana (false).
var respuesta = confirm("presiona boton");
if(respuesta === true)
{
    console.log("Has acepatado");
}
else
{
    console.log("Has cancelado");
}
window.prompt("Como te llamas"); // Pregunta al usuario y permite la escritura devolviendo el mensaje.
var nombre = prompt("Como te llamas");
