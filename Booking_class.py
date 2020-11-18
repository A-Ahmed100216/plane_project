# Is the ticket valid, is passport and visa valid for destination person is travelling to.
# Add to order details table
# Cost method
# Seat counter (See how many seats are available. If seat is sold, subtract from seats available before.)

# importing relevant modules
from db_connection_class import DB_Connection
from customer_class import Customer
import pandas as pd


class Booking(Customer):
    def __init__(self, adult_tickets, child_tickets, infant_tickets, passport_number, first_name, surname, tax_number):
        super().__init__(passport_number, first_name, surname, tax_number)
        self.available_seats = 400
        self.ticket_price = 100
        self.total_tickets = (adult_tickets + child_tickets + infant_tickets)
        self.adult_tickets = adult_tickets
        self.child_tickets = child_tickets
        self.infant_tickets = infant_tickets
        self.order_total = 0

    # asks the employee if the ticket, vis and passport are valid to travel
    def validation_check(self):
        if self.available_seats == 0:
            quit()
        check = input("Is the ticket, passport and visa valid for travel to destination? (Y/N)    ")
        if check.lower() == "y":
            self.total_cost()
        else:
            quit()

    # function to work out the total cost of the tickets
    def total_cost(self):
        print(f"There are currently {self.available_seats} seats remaining")
        tickets_ordered = 0

        if self.adult_tickets > 0:
            self.order_total += (self.adult_tickets * self.ticket_price)
            tickets_ordered += self.adult_tickets
            self.total_tickets += self.adult_tickets
        if self.child_tickets > 0:
            self.order_total += (self.child_tickets * (self.ticket_price * 0.75))
            tickets_ordered += self.child_tickets
            self.total_tickets += self.child_tickets
        if self.infant_tickets > 0:
            self.order_total += (self.infant_tickets * (self.ticket_price * 0.3))
            tickets_ordered += self.infant_tickets
            self.total_tickets += self.infant_tickets

        try:
            if tickets_ordered > self.available_seats:
                raise ValueError
        except ValueError:
            print("You have ordered too many tickets... Please try again")
            return
        else:
            pass

        print(f"\nYou have ordered {tickets_ordered} tickets: \n"
              f"{self.adult_tickets} Adult tickets \n"
              f"{self.child_tickets} Child tickets \n"
              f"{self.infant_tickets} Lap Child tickets \n"
              f"Your order total is £{self.order_total} \n")

        confirmation = input("Would you like to continue with the purchase? (Y/N)    ")
        if confirmation == "y":
            self.seat_counter(self.adult_tickets, self.child_tickets)
            self.order_details(self.adult_tickets, self.child_tickets, self.infant_tickets, self.order_total)
        else:
            return

    def seat_counter(self, adult_tickets, child_tickets):
        if adult_tickets > 0:
            self.available_seats -= adult_tickets
        if child_tickets > 0:
            self.available_seats -= child_tickets
        return print(f"There are {self.available_seats} seats remaining on the flight \n \n")

    def order_details(self, adult_tickets, child_tickets, infant_tickets, order_total):

        self.test.cursor.execute(f"""INSERT INTO Booking_Details
                                (Order_ID, Flight_ID, infant_tickets, child_tickets, adult_tickets, total_price)
                        VALUES
                                (Order_ID, Flight_ID, {infant_tickets}, {child_tickets}, {adult_tickets}, {order_total})
                        """)
        self.test.connection.commit()

        exported_data = pd.read_sql_query(
            f'SELECT *  FROM #booking_table# WHERE First_name = {self.first_name}',
            self.test.connection)
        df = pd.DataFrame(exported_data)

        "Here are the details of your order \n" \
        f"{df}"

    def amend_booking(self):
        self.test.cursor.execute(
            f'DELETE FROM Booking_Details where first_name = {self.first_name}')
        print("The booking has been deleted")
