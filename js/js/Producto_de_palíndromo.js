/*
Un número palindrómico se lee igual en ambos sentidos. El palíndromo más grande hecho del producto de dos números de 2 dígitos es 9009 = 91 × 99.

Encuentra el palíndromo más grande hecho del producto de dos números de 3 dígitos.
*/

function Palindromico(num)
{
    var producto = 0;
    
    if(num > 99 && num < 1000)
    {
        producto = num * (num + 1);
    }

    if(num === 99 || num === 1000)
    {
        producto = 100;
    }
    
    return producto;    
}

function Resultado()
{
    var R = 0;
    for(let i = 100; i <= 999; i++)
    {
        if(Palindromico(i) % i === 0)
        {
            R = Palindromico(i);
        }
    }
    return R;
}
console.log(Resultado());