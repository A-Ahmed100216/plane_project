import pandas as pd
import hashlib
from db_connection import DB_Connection
from booking import Booking
from flight_trip import Flight_Trip
from customers import Customer
from aircraft_class import Aircraft


class User_functions(DB_Connection):
    def __init__(self):
        super().__init__()
        self.functions = ["Create Flight Trip", "Add Passengers to flight trip", "Assign Plane", "Book Flight",
                          "Generate Flight Attendees", "Logout"]


    def login(self):
        while True:
            username=input("Please enter your username:  ")
            password=input("Please enter your password:  ")
            encodedpass=hashlib.md5(password.encode()).hexdigest()
            exists=self.cursor.execute(f"SELECT * FROM [admin] WHERE username='{username}'and password='{encodedpass}'").fetchall()
            if exists:
                return self.user_interface()
            else:
                print("Invalid password or username. Please try again")

    def user_interface(self):
        print("Welcome to BADA Airlines!")
        user_input = input("Which function would you like to use? \n"
                           "1. Create a flight trip \n"
                           "2. Add Passengers to flight trip\n"
                           "3. Assign Plane \n"
                           "4. Book Flight \n"
                           "5. Generate Flight Attendees \n"
                           "6. Log Out\n")

        if user_input=="1":
            trip=Flight_Trip()
            return trip.add_flight()

        if user_input == "2":
            flight_id=input("Please enter the destination or flight id you wish to add a passenger to:   ")
            passport_number=input("Please enter passport number:  ")
            first_name=input("Please enter  first name:   ")
            surname=input("Please enter last name:   ")
            tax_number=input("Please enter tax number:  ")
            gender = input("Please enter gender:  ")
            boarded_flight=input("Has the customer boarded the flight? 1=Yes 0=No  ")
            customer = Customer(passport_number, first_name,surname,tax_number)
            customer.add_to_customer_table(passport_number, first_name, surname,tax_number, flight_id, gender, boarded_flight)


        if user_input == "3":
            flight=Flight_Trip()
            print("We have the following crafts available in our fleet:  ")
            exported_data = pd.read_sql_query('SELECT * FROM aircraft', self.connection)
            df_2 = pd.DataFrame(exported_data)
            print(df_2)
            flight.add_flight()



        elif user_input == "4":
            book = Booking()
            book.validation_check()
            book.total_cost()
            book.seat_counter()

        elif user_input== "5":
            self.generate_attendees()

        elif user_input=="6":
            exit()
        else:
            print("Invalid input")

    def generate_attendees(self):
        flight_id = input("What is the flightID?    ")
        query=(f"SELECT Customers.PassportID, Customers.FirstName, Customers.Surname, Customers.Gender, Flight_Trip.Destination, Customers.Boarded_Flight FROM Customers INNER JOIN Flight_Trip ON Customers.Flight_ID=Flight_Trip.Flight_ID WHERE Customers.Flight_ID='{flight_id}' and Customers.Boarded_Flight='1'")

        exported_data = pd.read_sql_query(query,self.connection)
        df_2 = pd.DataFrame(exported_data)
        print(df_2)

        generate_csv = input("Would you like to generate a csv file of the flight attendees? (Y/N)    ")
        if generate_csv.lower() == "y":
            file_path = input("Please enter the location you would like the csv file    ")
            file_name = input("What would you like the file name to be called?    ")
            df_2.to_csv(fr'{file_path}\{file_name}.csv')
        else:
            return self.user_interface()


test = User_functions()
test.login()

# while True:
#     test.user_interface()