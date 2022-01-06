//Convertir tipos de datos

let valor;

//Convertir numero a texto
valor = String(6+5);

//Convertir boleano
valor=String(false);

//Convertir fecha a texto
valor = String(new Date());

//Convertir arreglo a texto
valor = String([1,2,3,4,5,6,7,8]); 

//Metodo toString() 
valor = (7).toString();
//Convertir fecha a texto
valor = new Date().toString();

//  Convertir string a números
valor = Number('7');
valor = Number(true); 
valor = Number(null);
valor = Number([1,2,3,4]); // no se puede no es un numero

//parseInt
valor = parseInt('32');
valor = parseFloat('72.28')

//Salidas en consola
console.log(valor);
console.log(typeof valor);
//console.log(valor.length); // Length sirve solo para texto
console.log(valor.toFixed(1)); // toFixed(1) sirve solo para numeros y en los parentisis mencionas el numero de decimales que necesitas

const valor1 = String(7);
const valor2 = 8;

const sumar  = Number(valor1) + valor2;

console.log(sumar);
console.log(typeof sumar);