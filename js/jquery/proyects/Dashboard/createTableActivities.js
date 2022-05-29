export function createTableActivities(dataActivities) {
    if(!(dataActivities?.date_activities)) {
        
    }

    return `
        <tr>
            <th>${dataActivities?.name_activities}</th>
            <td>${dataActivities?.description_activities}</td>
            <td>${dataActivities?.activities_focus}</td>
            <td>${dataActivities?.date_activities}</td>
        </tr>
    `;
}
