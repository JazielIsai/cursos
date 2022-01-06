/*
    2^15 = 32768 y la suma de sus dígitos es 3 + 2 + 7 + 6 + 8 = 26.

¿Cuál es la suma de los dígitos del número 2^1000 ?
*/

function SumaDijitos()
{
    let num = Math.pow(2,1000);
    var dijitos = String(num);
    dijitos.split();
    let suma = 0;
    var array = [dijitos.split()];
    console.log(dijitos);    
    array.forEach(function (dijitos)
    {   
        suma += dijitos;
        
    });
    return suma;
}

var Resultado = SumaDijitos();
console.log(Resultado);