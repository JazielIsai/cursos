var multiplo = 0;
for(i = 0; i < 1000; i++)
{
    if(i % 3 === 0 || i % 5 === 0)
    {
        multiplo += i;
    }
}
console.log("La suma de los multiplos del 3 y 5 es: ", multiplo);