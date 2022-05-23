

const button = document.querySelector('.button');
 
button.addEventListener('click', () =>{
    Notification.requestPermission()
        .then(result => console.log('Permission granted: ', result))
});

if(Notification.permission == 'granted'){
    new Notification('Esta es una notificacion', {
        icon: 'img/code.png',
        body: 'Notificacion personalida de Jaziel'
    })
}