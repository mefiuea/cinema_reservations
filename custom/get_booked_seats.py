def get_booked_seats(reservation_instance):
    """Function used to check reserved seats.
    Returns: list"""
    booked_seats_list = []
    for reservation in reservation_instance:
        for seat in reservation.booked_seats.all():
            booked_seats_list.append(seat.position)

    # print('BOOKED SEATS LIST: ', booked_seats_list, flush=True)
    return booked_seats_list
