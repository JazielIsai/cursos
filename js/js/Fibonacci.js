var valor = 4;
var numeros;

//Recursion 
function SerieFibonacci(num)
{
    //Caso inductivo
    if(num > 1)
    {
        numeros = SerieFibonacci(num -1) + SerieFibonacci(num -2); 
    }

    //Caso base
    if(num === 1)
    {
        numeros = 1;
    }

    return numeros;
}

function SumaParFibonacii()
{
    let suma = 0;
    let i = 1;
    while(SerieFibonacci(i) <= 4000000)
    {
        if(SerieFibonacci(i) % 2 === 0)
        {
            suma += SerieFibonacci(i);
        }
        i++;
    } 
    return suma;
}

console.log(String(SumaParFibonacii()));
