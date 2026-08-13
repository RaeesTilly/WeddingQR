class Bus:
    def __init__(self, route, avail_seats):
        self.route = route
        self.avail_seats = avail_seats
        self.order = []

    def get_seat(self, passenger):
        if self.avail_seats > 0:
            self.avail_seats -= 1
            self.order.append(passenger)
            print(f'booking successful: {passenger.nme}'
                  f'(tickets: {passenger.tickets_id})'
                  f'passanger booked a ticket for route {self.route}')
            print(f'Availble seats: {self.avail_seats}')
            return True

        else:
            print(f'Booking failed: {passenger.nme} there are no seats availble {self.route}')
            return False

    def show_info(self):
        print(f'Route: {self.route}')
        print(f'Available seats: {self.avail_seats}')
        print(f'Total number of bookings: {len(self.order)}')
        print()

class Passenger:
    def __init__(self, nme, tickets_id):
        self.nme = nme
        self.tickets_id = tickets_id

buses = [
    Bus("johannesburg - Freestate", 5),
    Bus("durban - johannesburg", 2)
]

passengers = [
    Passenger("Raees", "B101"),
    Passenger("Momo", "B102"),
    Passenger("kyle", "B103")
]

print("TransitFlow Bus routes")

for passenger in passengers:
    buses[0].get_seat(passenger)

for bus in buses:
    bus.show_info()
                