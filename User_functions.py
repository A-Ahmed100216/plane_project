# import pyodbc
import pandas as pd
from db_connection_class import DB_Connection
from Booking_class import Booking


class User_functions(DB_Connection, Booking):
    def __init__(self):
        super().__init__()
        self.functions = ["Create Flight Trip", "Add Passengers to flight trip", "Assign Plane", "Book Flight",
                          "Generate Flight Attendees", "Logout"]

    def user_interface(self):
        user_input = input("Which function would you like to use? \n"
                           f"{self.functions}\n"
                           f"")

        # if user_input.lower() == "create flight trip":

        # if user_input.lower() == "add passengers to flight trip":

        # if user_input.lower() == "assign plane":

        if user_input.lower() == "book flight":
            self.book_flight()

        if user_input.lower() == "generate flight attendees":
            self.generate_attendees()

        if user_input.lower() == "logout":
            exit()

    def generate_attendees(self):
        # flight_id = input("What is the flightID?    ")
        exported_data = pd.read_sql_query(
            f'SELECT CONCAT(ContactTitle, ContactName) AS "Name" FROM Customers ORDER BY ContactName ASC',
            self.connection)
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
        book.validation_check()


test = User_functions()
book = Booking()
while True:
    test.user_interface()
