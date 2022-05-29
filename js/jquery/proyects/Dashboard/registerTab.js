import {createCardClub} from "./createClub.js";
import {createCardEvent} from "./createEvents.js";
import {createTableActivities} from "./createTableActivities.js";

// call the form for create clubs
let $create_club_btn = $("#create_club_btn");
let $create_event_btn = $("#create_event_btn");
let $create_activity_btn = $("#create_activity_btn");


let $section_create_form = $(".section_create_form");


// crrate the form and save in the section
let $add_card_club = $("#submit_form_create_club");
let $add_card_event = $("#submit_form_create_event");
let $add_table_activities = $("#submit_form_create_activities");


let $section_cards_clubs = $(".section_cards_clubs");
let $section_cards_events = $(".section_cards_events");
let $add_row_activities = $(".table_body_activities")

$create_club_btn. on("click", function(){
    $section_create_form.toggle(300);
});

$add_card_club.on("click", function(e){
    e.preventDefault();
    $section_cards_clubs.append(createCardClub());
});

$create_event_btn.on("click", function(){
    $section_create_form.toggle(300);
});

$create_activity_btn.on("click", function(){
    $section_create_form.toggle(300);
});


$add_card_event.on("click", function(e){
    e.preventDefault();
    $section_cards_events.append(createCardEvent());

})

$add_table_activities.on("click", function(e){
    e.preventDefault();
    $add_row_activities.append(createTableActivities());
})

$(document).ready(function(){
    $section_create_form.hide();

});