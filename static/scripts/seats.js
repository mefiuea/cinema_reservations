/*
Function used for cinema hall view (booking_view). It is responsible for stylish changes on the website and provides
information about selected seats to view.
 */

window.addEventListener('DOMContentLoaded', (event) => {

    // get list of all available seats
    let available_seats_list = Array.from(document.getElementsByClassName('box-available'));

    // get list of booked seats from server and compare with all available seats
    let booked_seats_list = Array.from(document.getElementsByClassName('booked-seats'));
    booked_seats_list.forEach(function (booked_seat) {
        available_seats_list.forEach(function (available_seat) {
            if (available_seat.innerText === booked_seat.innerText) {
                console.log('MATCH!!!', available_seat.innerText, booked_seat.innerText)
                // marking reserved seats to red
                available_seat.classList.add('box-unavailable');
                available_seat.classList.remove('box-available');
                available_seat.id = 'unavailable';
            }
        })
    })

    function seats() {
        // when click on an empty seat (green), its color and status change to 'selected'
        let id_status = this.id;
        if (id_status === 'available') {
            this.classList.add('box-selected');
            this.classList.remove('box-available');
            this.id = 'selected';
        } else if (id_status === 'selected') {
            this.classList.add('box-available');
            this.classList.remove('box-selected');
            this.id = 'available';
        }

        // check if some places are picked
        let picked = document.getElementsByClassName('box-selected');
        // get 'Book ticket!' button element
        let book_ticket_button = document.getElementById('book-ticket');
        // checking how many places are selected. If more than 6 then it is not possible to book - disable button
        if (picked.length > 0 && picked.length < 7) {
            // seats are selected - enable button
            book_ticket_button.disabled = false;
        } else {
            // no seats selected - disable button
            book_ticket_button.disabled = true;
        }
    }

    function book() {
        // get list of selected seats
        let seats_array = Array.from(document.getElementsByClassName('box-selected'))
        let seats_list = []
        // iterator for label and input checkbox
        let id = 1
        // assigning appropriate properties to selected seats - those marked with the 'box-selected' class
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
        // console.log(seats_list);

        // everything ok - send form
        document.getElementById('book-ticket-form').submit();
    }

    $(document).ready(function () {
        // selecting only those elements (seats) that have an available class (they are green) and
        // activating the function after clicking on them
        let seat_selected = $('.box-available');
        seat_selected.click(seats);
        // selecting and running the 'Book ticket!' button on the cinema hall view page
        let book_ticket_button = $('#book-ticket');
        book_ticket_button.click(book);
    });
});
