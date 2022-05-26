$(document).ready(function() {
    $(".toggle").click(function() {
        console.log("clicked");
        $(".expandable_content").toggleClass("active");
        $(".toggle").toggleClass("active");
    })
})