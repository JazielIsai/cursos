let $registerNav = $("#dropdown-register");
let $registerContentNav = $("#dropdown-lvl1");

let $tracingNav = $("#dropdown-tracing");
let $tracingContentNav = $("#dropdown-lvl2");

let $consultNav = $("#dropdown-consult");
let $consultContentNav = $("#dropdown-lvl3")

let $administrationNav = $("#dropdown-administration");
let $administrationContentNav = $("#dropdown-lvl4");

let $option_register = $(".option-register");
let $section_create = $("section")


$registerNav.on("click", function(){
    $registerContentNav.toggle(300);
})

$tracingNav.on("click", function(){
    $tracingContentNav.toggle(300);
})

$consultNav.on("click", function(){
    $consultContentNav.toggle(300);
})

$administrationNav.on("click", function(){
    $administrationContentNav.toggle(300);
})

$(document).ready(function(){

    let btn_state = true;
    $option_register.on("click", function(e){
        if(btn_state){
            btn_state = !btn_state;

            let index = $option_register.index(this);
            console.log(index)
            
            // $(".section_create").removeClass("show")
            // $(".section_create").addClass("hide")
            // if(index == 0){
            //     $(".section_create_club").addClass("show");
            // } else if (index == 1){
            //     $(".section_create_abilities").addClass("show");
            // } else if (index == 2){
            //     $(".section_create_events").addClass("show");
            // }

            $section_create.removeClass("show");
            $section_create.addClass("hide");
            $section_create.eq(index).addClass("show");

            setTimeout(()=> {
                btn_state = !btn_state;
            }, 500);
        }
    })

})