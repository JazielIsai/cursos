var route = {
    _routes: {},
    add: function(url, action){
        this._routes[url] = action;
    },
    run: function(){
        $.each( this._routes, function(patron){
            if(location.href.match(patron)){
                //ejectuar cualquier código
                this();
            }
        });
    }
}


route.add('001.html', function(){
    console.log("This code alone works in the page 001.html");

});

route.add('.*.html', function(){
    console.log("This code works any page .html");

});

route.run();