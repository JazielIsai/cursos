
$( function () {

    $(document).on("contextmenu", function (e){
        e.preventDefault();
        // console.log(event)

        $(".menu").remove();

        let menu = $("<div>",{
            "class": "menu",
            "css": {
                "top": e.offsetY,
                "left": e.offsetX
            },
            "animate": {
                "width": "100px",
                "height": "300px",
            }
        })

        menu.appendTo('body');

    });

});