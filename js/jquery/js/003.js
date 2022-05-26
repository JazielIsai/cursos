var $element =  $(".element");

// is a div?
$element.is("div") && console.log("Es un div");

// do have the class element?
$element.is(".element") && console.log("The class element");

// this invisible
$element.is(":not(:visible)") && console.log("El element es invisible");

//elemento visibles
$element.is(":visible") && console.log("El element es visible");

//animación a
$element.animate({width:200},1000);

//esta animado 
$element.is(":animated") && console.log("El element is animade");
