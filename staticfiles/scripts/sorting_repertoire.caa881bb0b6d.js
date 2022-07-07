/*
Function used for repertoire view (get_repertoire_by_selected_sorting).
It is responsible for passing all user filtering and sorting data to the view.
 */

window.addEventListener('DOMContentLoaded', (event) => {

    function sorting_filtering() {
        // selecting only radio button that was selected during filtering
        let marked_radio_button = document.querySelector('input[name="sorting"]:checked').value;
        // get actually date
        let date_from_calendar = document.querySelector('input[name="date"]').value;
        // get selected genre
        let genres = document.getElementById("genre-names");
        let genre = genres.options[genres.selectedIndex].value;
        // create query string
        let params = new URLSearchParams();
        params.append("sorting_by", marked_radio_button)
        params.append("date", date_from_calendar)
        params.append("genre", genre)
        // indication of url path to which the request is to be sent
        let address = 'get_repertoire_by_selected_sorting/?' + params.toString();
        // View call (get_repertoire_by_selected_sorting) with parameters. Waiting for a response.
        // Collecting the response from the view in html and replacing this data on the main page with views.
        let vf = fetch(address).then(function (response) {
            return response.text();
        }).then(function (data) {
            // get list of repertoires and replacement of data from the received response
            return document.getElementById('repertoires').innerHTML = data;
        })

        // update date
        let actual_date = document.getElementById('actual-date').innerText = date_from_calendar
        console.log(actual_date)
    }

    $(document).ready(function () {
        // select radio button in sorting option
        let radio_checked = $('.form-check-input');
        radio_checked.click(sorting_filtering);
        // select drop-down menu in filtering option
        let genre_selected_menu = $('#genre-names');
        genre_selected_menu.change(sorting_filtering);
    });

});
