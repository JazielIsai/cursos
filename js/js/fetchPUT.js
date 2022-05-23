let bodyRequest = {
    'id_workflow': 2,
    "x_axis":202,
    "y_axis":219
}

let formData = new FormData();
formData.append('id_workflow', 1);
formData.append('x_axis', 32);
formData.append('y_axis', 324);

let requestPUT = {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(bodyRequest)
}

function RequestPUT () {
    fetch('http://localhost/WebServices-version-tres/webServices.php', requestPUT)
        .then(data => data.json())
        .then(response=> console.log(response))
}

RequestPUT();