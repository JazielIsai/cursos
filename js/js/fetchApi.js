//Fetch Api es el nuevo estandar 
//igual que ajax te permite eviar informacion al servidor u obtener informacion de un servidor
//permite que podamos actualizar el sittio web sin actualizar la pagina
//puede obtener un archivo local o una respuesta de un servidor (texto u json)
//Al igual que todas las Api's modernas de Javascript utiliza promises o tambien async / await

//Json significa JavaScript object notation, este es un lenguaje de transporte de datos 

//Un json puede ser creado en cualquier lenguaje y se puede consumir en javascript por medio de fetch Api y mostrarlo en tu sitio web
//Asi que tanto en Java, c#, Python, Node JS, PHP, pueden exportar una respuesta en formato json y podemos leerlos con fetch para poder mostrarlos en la web

//Codigo de fetch api con promises
/*
function obtenerEmpleado() {
    //fetch --> es una funcion que ya existe en javascript, y recibe como parametro una url o un archivo json
    const archivo = './js/empleados.json';
    fetch(archivo)
        .then(response => {
            return response.json();
        })
        .then(datos => {
            const {empleados} = datos;
            
            empleados.forEach(empleado => {
                empleado.id > 0 ? document.querySelector('p').textContent += ' ' + empleado.name : document.querySelector('p').textContent = 'No hay ninguno';

            })

            console.log(datos);
        })
        .catch(err => {
            console.log(err);
        })
        
        
}
    
    obtenerEmpleado();
*/


//uso de fetch api con async / await


async function obtenerEmpleados() {
    let categoria = [  ];

    const archivo = 'http://viperdb.scripps.edu/Lab/Workflow/nodes.php?serviceName=get_nodes';

    const resultado = await fetch(archivo);
    console.log(resultado)
    const datos = await resultado.json();
    console.log(datos);

    // categoria = datos.map( dt => {
    //     return dt.category
    //     // if( categoria.includes( data.category )  ){
    //     // } else {
    //     //     categoria.push(data.category);
    //     // }
    // } )

    // categoria = datos.reduce( (acc, node, index) =>{
    //     acc[node.category] = ( acc[node.category] || '' ) + [node.name, node.idnode, ' '] 
    //     return acc;
    // }, {} )

    categoria = datos.reduce( (category, node, key) => {
        (category[node.category] || (category[node.category] = [])).push( { name: node.name, idnode: node.idnode } );
        return category
    }, {} )

    const categorias = datos.map( category => category.category )
    // let includeCategory;

    // for (getNodeForCategory in data) {
        
    // }

    return categoria;

}

let dt;

obtenerEmpleados()
    .then( (data) => { 
       dt = data 
       
       console.log("datos: ", dt)
       
       

    });


