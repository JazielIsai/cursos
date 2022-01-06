class Enamorados
{
    constructor()
    {

    }

    Se_Gustan(boleano)
    {
        let desicion; 
        if(boleano == true)
        {
            desicion = "Se gustan";
        }
        else{
            desicion = "No se gustan";
        }
        return desicion;
    }
}

class Compatibles extends Enamorados
{
    constructor()
    {

    }
    
    Personalidad(boleano)
    {
        let desicion = "";
        if(boleano == true)
        {
            desicion = "Compatible";
        } 
        else 
        {
            desicion = "Incompatible";
        }
        return desicion;
    }
}

class Boda extends Compatibles
{
    constructor()
    {

    }

    Es_Verdadero(boleano)
    {
        let desicion;
        if(boleano == true)
        {
            desicion = "Se casan";
        } 
        else
        {
            desicion = "No se casan";
        }
        return desicion;
    }
}

class Resultado extends Boda
{
    constructor()
    {
        
    }

    Love(desicion)
    {
        while(desicion)
        {
            document.write(super.Se_Gustan(desicion));
            document.write(super.Personalidad(desicion));
            document.write(super.Es_Verdadero(desicion));
            break;
        }
        return desicion;
    }
}

var I = new Resultado();
I.Love(true);
