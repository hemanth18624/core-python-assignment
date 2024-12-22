def display_available_seats(total_seats, booked_seats):
    return [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]

def book_seat(seat_number, total_seats, booked_seats):
    if seat_number < 1 or seat_number > total_seats:
        return "Invalid seat number."
    if seat_number in booked_seats:
        return "Seat already booked."
    booked_seats.append(seat_number)
    return f"Seat {seat_number} booked successfully."

def cancel_seat(seat_number, booked_seats):
    if seat_number not in booked_seats:
        return "Seat not booked yet."
    booked_seats.remove(seat_number)
    return f"Seat {seat_number} cancelled successfully."


total_seats = 10
booked_seats = [2, 5, 7]

book_seat_number = 3
print(book_seat(book_seat_number, total_seats, booked_seats))


cancel_seat_number = 5
print(cancel_seat(cancel_seat_number, booked_seats))


available_seats = display_available_seats(total_seats, booked_seats)
print("Available seats:", available_seats)
