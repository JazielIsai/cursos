let mHeaders = new Headers({'Content-Type':'application/json'});

let bodyPost = {
    // "workflow_content_id":34,
    // "workflow_id":2,
    "x_axis":202,
    "y_axis":219
}
bodyPost = JSON.stringify(bodyPost)

let formData = new FormData()

formData.append('x_axis', 202)
formData.append('y_axis', 209)

// console.log(formData, 'form data', bodyPost, 'body post')

const requestPost = { 
    method: "POST",
    // redirect: 'follow',
    body:  formData,
    // headers: mHeaders,
    // mode: 'cors', // no-cors, *cors, same-origin
    // cache: 'default', // *default, no-cache, reload, force-cache, only-if-cached
    // credentials: 'omit', // include, *same-origin, omit
    // // referrerPolicy: "unsafe-url"
    // redirect: 'follow', // manual, *follow, error
    // referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
}

function ChangePositionNodes() {

    

    // const url = 'http://192.168.0.101/workflow_backend/services.php?serviceName=update_node_position';

    // axios.post(url, {
    //     params: {
    //         update_info: `{
    //             "workflow_content_id":34,
    //             "workflow_id":2,
    //             "x_axis":202,
    //             "y_axis":101
    //         }`
    //     }
    // })
    //     .then(res => {
    //         console.log(res);
    //     })
    //     .catch(err => {
    //         console.log(err);
    //     })



    // var dataSend = new FormData();
    // dataSend.append('update_info', `{
    //     "workflow_content_id":34,
    //     "workflow_id":2,
    //     "x_axis":202,
    //     "y_axis":101
    // }`);
    // var request = new Request('http://192.168.0.101/workflow_backend/services.php?serviceName=update_node_position', {
    //     method: 'POST',
    //     body:  dataSend
    // });
    // console.log('request = ', request);



    fetch('http://localhost/WebServices-version-tres/webServices.php', requestPost )
            .then((response) => {
              return response.text();
            })
            .then ( response => console.log(response) )
            

    console.log('Prueba')
}


ChangePositionNodes()