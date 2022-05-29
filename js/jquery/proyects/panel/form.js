export function createForm ( ) {
    let form = `
        <form class="form_create_club">
            <div class="form-group">
                <label for="name_club"> Name Club: </label>
                <input type="text" class="form-control" id="name_club" placeholder="Ej: Ajedrez" name="name_club" />
            </div>
            <div class="form-group">
                <label for="description_club"> Descripción Club: </label>
                <input type="text" class="form-control" id="description_club" placeholder="Descripción... " name="description_club" />
            </div>
            <div class="form-group">
                <label for="manager_club"> Lider del club: </label>
                <input type="text" class="form-control" id="manager_club" placeholder="Lider..." name="manager_club" />
            </div>
            <div class="form-group">
                <label for="objective_club"> Objetivo del Club: </label>
                <input type="text" class="form-control" id="objective_club" placeholder="Objetivo..." name="objective_club" />
            </div>
            <div class="form-group submit_create_club_wrap_btn">
                <input type="submit" class="btn btn-success" value="Crear" id="submit_form_create_club" />
            </div>
        </form>
    `

    return form;
}

