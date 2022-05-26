$(".listLinks a").each(function(){
    console.log( this.hostname )

    if( this.hostname !== location.hostname ){
        $(this).append("<img src='https://cdn-icons-png.flaticon.com/512/376/376209.png'/>")
            .attr("target",'_blank')
    }
})