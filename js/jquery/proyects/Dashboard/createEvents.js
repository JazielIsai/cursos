export function createCardEvent(dataEvent) {
    return `
    <div class="movie_card" id="bright">
        <div class="info_section">
            <div class="movie_header">
                <img class="locandina" src="https://www.elsoldedurango.com.mx/incoming/lbc3vb-torneo-de-ajedrez-en-movimiento/ALTERNATES/LANDSCAPE_960/Torneo%20de%20Ajedrez%20en%20Movimiento"/>
                <div>
                    <h2> ${dataEvent?.name_event} </h2>
                    <h4> ${dataEvent?.date_event} </h4>
                    <span class="minutes"> ${dataEvent?.time_event} </span>
                    <p class="type"> ${dataEvent?.place_event} </p>
                </div>
            </div>
            <div class="movie_desc">
                <p class="text">
                    ${dataEvent?.description_event}
                </p>
            </div>
            <div class="movie_social">
                <ul>
                    <li>
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pen" viewBox="0 0 16 16">
                            <path d="m13.498.795.149-.149a1.207 1.207 0 1 1 1.707 1.708l-.149.148a1.5 1.5 0 0 1-.059 2.059L4.854 14.854a.5.5 0 0 1-.233.131l-4 1a.5.5 0 0 1-.606-.606l1-4a.5.5 0 0 1 .131-.232l9.642-9.642a.5.5 0 0 0-.642.056L6.854 4.854a.5.5 0 1 1-.708-.708L9.44.854A1.5 1.5 0 0 1 11.5.796a1.5 1.5 0 0 1 1.998-.001zm-.644.766a.5.5 0 0 0-.707 0L1.95 11.756l-.764 3.057 3.057-.764L14.44 3.854a.5.5 0 0 0 0-.708l-1.585-1.585z"/>
                        </svg>
                        Edit
                    </li>
                    <li>
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-up-right-circle" viewBox="0 0 16 16">
                            <path fill-rule="evenodd" d="M1 8a7 7 0 1 0 14 0A7 7 0 0 0 1 8zm15 0A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM5.854 10.803a.5.5 0 1 1-.708-.707L9.243 6H6.475a.5.5 0 1 1 0-1h3.975a.5.5 0 0 1 .5.5v3.975a.5.5 0 1 1-1 0V6.707l-4.096 4.096z"/>
                        </svg>
                        Ir a
                    </li>

                </ul>
            </div>
        </div>
    </div>
    `
}