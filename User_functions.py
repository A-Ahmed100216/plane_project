import pyodbc
import pandas as pd
from Booking_class import Booking


class User_functions(Booking):
    def __init__(self, adult_tickets, child_tickets, infant_tickets, passport_number, first_name, surname, tax_number):
        super().__init__(adult_tickets, child_tickets, infant_tickets, passport_number, first_name, surname, tax_number)
        self.functions = ["1. Create Flight Trip", "2. Add Passengers to flight trip", "3. Assign Plane", "4. Book Flight",
                          "5. Delete Booking", "6. Generate Flight Attendees", "7. Logout"]

    def user_interface(self):
        user_input = input("Which function would you like to use? \n"
                           f"{self.functions}\n"
                           f"")

        # if user_input.lower() == "create flight trip":

        # if user_input.lower() == "assign plane":

        if user_input.lower() == "add passengers to flight trip" or "2":
            flight_id = int(input("What is your flight ID?    "))
            gender = input("What is your gender?   ")
            boarded_flight = int(input("Is the passenger boarding the flight? (0 / 1) "))

            self.add_to_customer_table(passport_number, first_name, surname, tax_number, flight_id, gender,
                                       boarded_flight)

        if user_input.lower() == "book flight" or "4":
            self.book_flight()

        if user_input.lower() == "delete booking" or "5":
            self.amend_booking()  # test this#

        if user_input.lower() == "generate flight attendees" or "6":
            self.generate_attendees()  # add SQL query for this #

        if user_input.lower() == "logout" or "7":
            exit()

    def generate_attendees(self):
        # flight_id = input("What is the flightID?    ")
        exported_data = pd.read_sql_query(
            f'SELECT *  FROM aircraft',
            self.test.connection)
        df_2 = pd.DataFrame(exported_data)
        print(df_2)

        generate_csv = input("Would you like to generate a csv file of the flight attendees? (Y/N)    ")
        if generate_csv.lower() == "y":
            file_path = input("Please enter the location you would like the csv file    ")
            file_name = input("What would you like the file name to be called?    ")
            df_2.to_csv(fr'{file_path}\{file_name}.csv')
        else:
            return

    def book_flight(self):
        self.validation_check()

    def amend_booking(self):
        self.amend_booking()


adult_tickets = int(input("How many adult tickets are you buying?    "))
child_tickets = int(input("How many child tickets are you buying?    "))
infant_tickets = int(input("How many infant tickets are you buying?    "))
passport_number = input("What is your passport number?    ")
first_name = input("What is your first name?    ")
surname = input("What is your Surname?    ")
tax_number = input("What is your tax number?    ")
test = User_functions(adult_tickets, child_tickets, infant_tickets, passport_number, first_name, surname, tax_number)
test.user_interface()
