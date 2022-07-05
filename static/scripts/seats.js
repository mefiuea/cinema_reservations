window.addEventListener('DOMContentLoaded', (event) => {
    console.log('test-seats')

    function seats() {
        let id_status = this.id;
        console.log('id status before: ', id_status)
        if (id_status === 'available') {
            this.classList.add('box-selected')
            this.classList.remove('box-available')
            this.id = 'selected'
            let id_status = this.id;
            console.log('id status after: ', id_status)
        }
        // this.classList.add('box-unavailable')
    }

    $(document).ready(function () {
        let seat_selected = $('.box-available, .box-unavailable');
        seat_selected.click(seats);
    });
});
