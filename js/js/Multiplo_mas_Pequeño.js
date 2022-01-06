//¿Cuál es el número positivo más pequeño que es divisible por todos los números del 1 al 20?
class MultiploPequeño
{
    constructor()
    {

    }
    //2,4,6,8,10,12,14,16,18,20
    //3,6,9,12,15,18,21
    //5,10,15,20
    //7,14,21
    //11,22
    //13
    //17
    //19

    Multilplo(boleano)
    {
        let minimo = 0;
        let num = 1;
        //mientras boleano sea true entra al ciclo
        while(boleano)
        {
            console.clear();
            if(num % 5 === 0 && num % 6 === 0 && num % 7 === 0 && num % 11 === 0 && num % 13 === 0 && num % 17 === 0 && num % 19 ===0)
            {
                minimo = num;
                boleano = false;
                document.write(num);
                break;
            }
            num++;
            console.log(num);
        }
        
        return minimo;
    }
}

var Objeto = new MultiploPequeño();

console.log(Objeto.Multilplo(true));