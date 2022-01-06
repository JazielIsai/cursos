function buildtree(num)
{
    let space = num * 2;
    for(var i = 0; i <= num; i++)
    {
        let n = 1;
        let y = i;
        let text = '';
        let addSpace = space;

        //
        while(addSpace > 0)
        {
            text = text + ' ';
            addSpace--;
        } 

        while(y > 0)
        {
            text = text + ' ' + y;
            y--;
        } 

        y = i;
        text = text = ' 0'; // agregar cero

        while(n <= i)
        {
            text = text + ' ' + n;
            n++;
        } 

        space = space - 2;
        addSpace = space;
        console.log(text);
    }
}

buildtree(5);