import {create_club_card} from './createClubs.js';
import {createForm} from './form.js';

let create_club =  $('.create_from_form');
let create_club_btn = $('#create_club_btn');
let add_form = $('#add_form');
let form_create_club = $('.form_create');
let cards_clubs = $('.card_club');
let submit_form_create_club = $('#submit_form_create_club');

let go_clubs = $('#go_club');
let go_activ = $('#go_activ');
let go_abilities = $('#go_abilities');
let go_events = $('#go_events');


create_club_btn.on('click', function(e) {
    form_create_club.toggle(1000);
});


submit_form_create_club.on("click", function(e) {
    e.preventDefault();
    cards_clubs.append(create_club_card());
});



$(document).ready(function() {
    form_create_club.hide();

    let nav_tab = $(".aside nav li .nav-link");
    let nav_item_tab = $(".aside nav li .nav-link").lenght + 1;
    let btn_state = true;

    nav_tab.on("click", function(e) {
        if(btn_state) {
            btn_state = !btn_state;

            let index = nav_tab.index(this);
            $("section").removeClass("show");
            $("section").addClass("hide");
            $("section").eq(index).addClass("show");

            setTimeout(() =>{
                btn_state = !btn_state;
            },500)

        }
    })


})


