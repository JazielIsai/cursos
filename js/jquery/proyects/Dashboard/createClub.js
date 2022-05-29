export function createCardClub(dataClub) {

    let form = ` 
    <a href="" class="card">
      <img src="https://liceumgm.com/wp-content/uploads/2018/07/club-de-ajedrez-liceum-3.jpg" class="card__image" alt="${dataClub.name_club}" />
      <div class="card__overlay">
        <div class="card__header">
          <svg class="card__arc" xmlns="http://www.w3.org/2000/svg"><path /></svg>                     
          <img class="card__thumb" src="https://pngimage.net/wp-content/uploads/2018/06/sme-icon-png-4.png" alt="" />
          <div class="card__header-text">
            <h3 class="card__title"> ${dataClub.name_club} </h3> 
            <h4 class="card__title"> ${dataClub.manager_club} </h4> 
            <div class="card__status_wrapper">
                <span class="card__status"> ${ dataClub?.student_club } </span>
                <span class="card__status">1 alumno</span>
            </div>           
          </div>
        </div>
        <p class="card__description"> ${dataClub.description_club} </p>
      </div>
    </a>      
    `
    return form;
}