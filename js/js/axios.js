

const url = 'http://viperdb.scripps.edu/Lab/Workflow/nodes.php?serviceName=get_nodes';

axios.get(url)
    .then( res => { 
        console.log(res)        
        return res.data
    } )
    .then( data => console.log(data[0]) )
    .catch( err => console.log(err))