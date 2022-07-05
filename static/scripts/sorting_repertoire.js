window.addEventListener('DOMContentLoaded', (event) => {
    // console.log('test');

    function checked_radio_button() {
        let marked_radio_button = document.querySelector('input[name="sorting"]:checked').value;
        let date_from_calendar = document.querySelector('input[name="date"]').value;
        let params_list = [marked_radio_button, date_from_calendar]
        console.log(marked_radio_button)
        console.log(date_from_calendar)
        console.log(params_list)
        let params = new URLSearchParams();
        params.append("sorting_by", marked_radio_button)
        params.append("date", date_from_calendar)
        console.log(params)
        let address = 'get_repertoire_by_selected_sorting/?' + params.toString();
        console.log(address)

        let vf = fetch(address).then(function (response) {
            return response.text();
        }).then(function (data) {
            return document.getElementById('repertoires').innerHTML = data;
        })

        // update date
        let actual_date = document.getElementById('actual-date').innerText = date_from_calendar
        console.log(actual_date)
    }

    $(document).ready(function () {
        // foundations
        let radio_checked = $('.form-check-input');
        radio_checked.click(checked_radio_button);
    });

});
