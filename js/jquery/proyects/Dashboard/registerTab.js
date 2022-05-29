import {createCardClub} from "./createClub.js";
import {createCardEvent} from "./createEvents.js";
import {createTableActivities} from "./createTableActivities.js";

// call the form for create clubs
let $create_club_btn = $("#create_club_btn");
let $create_event_btn = $("#create_event_btn");
let $create_activity_btn = $("#create_activity_btn");


let $section_create_form = $(".section_create_form");


// crrate the form and save in the section
let $add_card_club = $("#create_club_form");
let $add_card_event = $("#create_events_form");
let $add_table_activities = $("#create_activities_form");


// ---------------- THIS IS FOR ADD FOR APPEND  ---------------------------
let $section_cards_clubs = $(".section_cards_clubs");
let $section_cards_events = $(".section_cards_events");
let $add_row_activities = $(".table_body_activities")


// -----------  SHOW OR HIDE FORM ---------------- //
$create_club_btn. on("click", function(){
    $section_create_form.toggle(300);
});

$create_event_btn.on("click", function(){
    $section_create_form.toggle(300);
});

$create_activity_btn.on("click", function(){
    $section_create_form.toggle(300);
});


//ID OF FORM ------ SEND FOR FORM A THE DATABABSE AND CREATE CARD 
$add_card_club.submit(function(e){
    console.log(e)
    // Serializar el formulario, el fondo normalmente puede obtener datos a través del método de publicación
    let postDataObject = {};
    let postData = $add_card_club.serializeArray();
    $.each(postData, function(i, item){
        postDataObject[item.name] = item.value;
    })
    console.log("add_card_club ",postDataObject)

    $section_cards_clubs.append(createCardClub(postDataObject));
})

$add_card_event.submit(function(e){
    let postDataObject = {};
    let postData = $add_card_event.serializeArray();
    $.each(postData, (i, item) => {
        postDataObject[item.name] = item.value;
    })

    console.log("add_card_event", postDataObject)
    $section_cards_events.append(createCardEvent(postDataObject));

})

$add_table_activities.submit(function(e){
    let postDataObject = {};
    let postData = $add_table_activities.serializeArray();
    $.each(postData, (i, item) => {
        postDataObject[item.name] = item.value;
    })
    console.log("add_row_activities", postDataObject);
    $add_row_activities.append(createTableActivities(postDataObject));
})

//-----------------------------------------------------------//

$(document).ready(function(){
    $section_create_form.hide();

});