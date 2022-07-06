window.addEventListener('DOMContentLoaded', (event) => {

    function seats() {
        let id_status = this.id;
        // console.log('id status before: ', id_status)
        if (id_status === 'available') {
            this.classList.add('box-selected')
            this.classList.remove('box-available')
            this.id = 'selected'
            let id_status = this.id;
            // console.log('id status after: ', id_status)
        } else if (id_status === 'selected') {
            this.classList.add('box-available')
            this.classList.remove('box-selected')
            this.id = 'available'
            // console.log('id status after: ', id_status)
        }

    }

    function book() {

        // get list of selected seats
        let seats_array = Array.from(document.getElementsByClassName('box-selected'))
        let seats_list = []
        // iterator for label and input checkbox
        let id = 1
        seats_array.forEach(function (seat) {
            let label = document.createElement("label");
            label.setAttribute('for', 'seat-' + id)
            let check_box = document.createElement('input');
            check_box.type = 'checkbox';
            check_box.name = 'selected_seats';
            check_box.id = 'seat-' + id;
            check_box.value = seat.innerText;
            check_box.checked = true;
            label.appendChild(check_box);
            seat.appendChild(label);
            check_box.style.display = 'None'

            seats_list.push(seat.innerText);

            id += 1;
        })
        console.log(seats_list);

        // everything ok - send form
        document.getElementById('book-ticket-form').submit();

    }

    $(document).ready(function () {
        let seat_selected = $('.box-available');
        seat_selected.click(seats);
        let book_ticket_button = $('#book-ticket');
        book_ticket_button.click(book);
    });
});
