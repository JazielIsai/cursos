$("li", "#firstList").each(function(){
    console.log( $(this).html() )
})

var div = $('<div>', {
    'class': 'blue-grow',
    'css': {
        'background-color': 'blue'
    }, 
    'width': '30px',
    'height': '30px',
    'animate': {
        width: '250px',
        height: '50px',
    }
})

div.appendTo('body')