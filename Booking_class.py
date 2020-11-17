# Is the ticket valid, is passport and visa valid for destination person is travelling to.
# Add to order details table
# Cost method
# Seat counter (See how many seats are available. If seat is sold, subtract from seats available before.)


class Booking:
    def __init__(self, total_seats):
        self.available_seats = total_seats
        self.ticket_price = 100
        self.total_tickets = 0
        # self.adult_tickets = 0
        # self.child_tickets = 0
        # self.lap_child_tickets = 0


    def validation_check(self):
        check = input("Is the ticket, passport and visa valid for travel to destination? (Y/N)    ")
        if check.lower() == "y":
            self.total_cost()
        else:
            return

    def total_cost(self):
        tickets_ordered = 0
        order_total = 0
        adult_tickets = int(input("How many adult tickets would you like to purchase?    "))
        child_tickets = int(input("How many child tickets (ages 2-14) would you like to purchase?    "))
        lap_child_tickets = int(input("How many lap child tickets (ages 0-2) would you like to purchase?    "))

        if adult_tickets > 0:
            order_total += (adult_tickets * self.ticket_price)
            tickets_ordered += adult_tickets
            self.total_tickets += adult_tickets
        if child_tickets > 0:
            order_total += (child_tickets * (self.ticket_price * 0.75))
            tickets_ordered += child_tickets
            self.total_tickets += child_tickets
        if lap_child_tickets > 0:
            order_total += (lap_child_tickets * (self.ticket_price * 0.3))
            tickets_ordered += lap_child_tickets
            self.total_tickets += lap_child_tickets

        print(f"\nYou have ordered {tickets_ordered} tickets: \n"
        f"{adult_tickets} Adult tickets \n"
        f"{child_tickets} Child tickets \n"
        f"{lap_child_tickets} Lap Child tickets \n"
        f"Your order total is £{order_total} \n")

        confirmation = input("Would you like to continue with the purchase? (Y/N)    ")
        if confirmation == "y":
            self.seat_counter(adult_tickets, child_tickets)
            # self.order_details()
        elif confirmation == "n":
            return

    def seat_counter(self, adult_tickets, child_tickets):
        if adult_tickets > 0:
            self.available_seats -= adult_tickets
        if child_tickets > 0:
            self.available_seats -= child_tickets
        return print(f"There are {self.available_seats} seats remaining on the flight \n \n")


    def order_details(self):
        cursor.execute(f"""INSERT INTO bada_airlines
                                (OrderID, FlightID, lap_child_tickets, child_tickets, adult_tickets, total_price)
                        VALUES
                                (OrderID, FlightID, {self.lap_child_tickets}, {self.child_tickets}, {self.adult_tickets}, {self.order_total})
                        """)
        conn.commit()

test = Booking(400)
while True:
    test.validation_check()