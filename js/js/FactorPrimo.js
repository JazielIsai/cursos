const numero = 600851475143;

function Mayor_Factor_Primo(num)
{
    let mayor = 0;
    var primo = 0;
    var i = 0;
    while(i <= num)
    {
        if(num % i === 0) 
        {
            primo = i;
            document.write(String(primo));
            break;
        }
        i++;
    }
    
    return mayor;
}

console.log(String(Mayor_Factor_Primo(numero)));