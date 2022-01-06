//Encuentra la diferencia entre la suma de los cuadrados de los primeros cien números naturales y el cuadrado de la suma.
class SumSumCuadrada
{
    constructor()
    {

    }

    Suma_de_los_cuadrados(num)
    {
        //La suma de los cuadrados de los primeros diez números naturales es,
        //1 2 + 2 2 + ... + 10 2 = 385
        let suma = 0;
        for(var i = 1; i<= num; i++)
        {
            suma += Math.pow(i, 2);
        }
        return suma;
    }

    EL_Cuadrado_de_la_suma(num)
    {
        //El cuadrado de la suma de los primeros diez números naturales es,
        //(1 + 2 + ... + 10) 2 = 55 2 = 3025
        let suma = 0;
        let elevar = 0;
        for(var i = 1; i <= num; i++)
        {
            suma += i;
            elevar = Math.pow(suma, 2); 
        }
        return elevar;
    }

    Diferencia_de_los_cuadrados()
    {
        let diferencia = 0;
        diferencia =  this.EL_Cuadrado_de_la_suma(100) - this.Suma_de_los_cuadrados(100);
        return diferencia;
    }
}

//Objeto
var Dif = new SumSumCuadrada();

//console.log(String(Dif.Suma_de_los_cuadrados(10)));
//console.log(String(Dif.EL_Cuadrado_de_la_suma(10)));

var leer = Dif.Diferencia_de_los_cuadrados();
console.log(leer);
