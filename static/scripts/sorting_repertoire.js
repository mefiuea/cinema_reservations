window.addEventListener('DOMContentLoaded', (event) => {
    // console.log('test');

    function checked_radio_button() {
        let marked_radio_button = document.querySelector('input[name="sorting"]:checked').value;
        console.log(marked_radio_button)
        let params = new URLSearchParams();
        params.append("sorting_by", marked_radio_button)
        let address = 'get_repertoire_by_selected_sorting/?' + params.toString();
        console.log(address)

        let vf = fetch(address).then(function (response) {
            return response.text();
        }).then(function (data) {
            console.log('TUTAJ')
            // return document.getElementById('ins-pag').innerHTML = data;
        })
    }

    $(document).ready(function () {
        // foundations
        let radio_checked = $('.form-check-input');
        radio_checked.click(checked_radio_button);
    });

});
