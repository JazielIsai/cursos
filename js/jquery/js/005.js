$.fn.existing = function(){ return this.length > 0; };

console.log(  $("h1").existing() ? "existing" : "not existing")