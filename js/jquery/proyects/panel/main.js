let create_club =  $('.create_club');
let create_club_btn = $('#create_club_btn');
let form_create_club = $('.form_create_club');
let cards_clubs = $('.card_club');
let submit_form_create_club = $('#submit_form_create_club');


function create_club_card() {

    let form = ` 
        <div class="club">
            <div class="wrap_img_club">
                <img src="https://liceumgm.com/wp-content/uploads/2018/07/club-de-ajedrez-liceum-3.jpg" alt="ajedrez">
            </div>
            <div class="content_club">
                <h3 class="title_club" > Ajedrez </h3>
                <div class="data_card_club">
                    <p class="cant_club"> 10 alumnos </p>
                    <p class="status_club"> Al corriente </p>
                </div>
                <p class="manager_club"> <strong>Maximiliano Ruiz Manjarrez</strong> </p>
            </div>
            <div class="club_wrap_btn">
                <input type="button" value="Ir a club" id="ir_club" class="btn btn-secondary" />
            </div>
        </div>
    `
    return form;
}


create_club_btn.on('click', function(e) {
    form_create_club.toggle(1000);
})


submit_form_create_club.on("click", function(e) {
    e.preventDefault();
    cards_clubs.append(create_club_card());
})

$(document).ready(function() {
    form_create_club.hide();
})