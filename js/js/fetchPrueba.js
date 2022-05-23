
let dataJson;
const select = document.querySelector('#seleciona');


fetch('http://viperdb.scripps.edu/Lab/Workflow/nodes.php?serviceName=get_nodes')
    .then( pros => pros.json() )
    .then( data => { 
        data.map( els => { 
            select.innerHTML += `
                    <option value="${els.name}">
                        ${els.name}
                    </option>
                `
         })

     } )



     
// import React, { useState, useEffect } from 'react';

// function fetchPrueba() {
//     const [ dataLoad, setDataLoad ] = useState( [] )

//     function loadingData(){
//         fetch('http://viperdb.scripps.edu/Lab/Workflow/nodes.php?serviceName=get_nodes')
//     .then( pros => pros.json() )
//     .then( data => { 
//             setDataLoad(data)

//      } )
//     }

//     useEffect ( ()=> {
//         loadingData()
//     }, [] )
  
//     return (
//         <div>
//             {
//                 dataLoad.map( els => { 
//                     <compoen1 
//                         di = { els.idnode }
//                         name = { els.name }
//                     />
//                  })
        
//             }
//         </div>
//     );
// }

// export default fetchPrueba;
