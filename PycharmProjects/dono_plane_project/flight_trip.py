import pyodbc
import pandas
from aircraft import Aircraft

class Flight_Trip(Aircraft):
    def __init__(self):
        super().__init__()

    def create_table(self):
        self.cursor.execute("CREATE TABLE Flight_Trip (Flight_ID INT NOT NULL IDENTITY(1,1) PRIMARY KEY, craft_id INT, Destination VARCHAR(100), Duration_hrs INT, Scheduled VARCHAR(100));")


    def view_table(self):
        flights_table = self.cursor.execute("SELECT * FROM Flight_Trip").fetchall()
        return flights_table

    def existing_flights(self):
        self.cursor.execute("INSERT INTO Flight_Trip (craft_id, Destination, Duration_hrs, Scheduled) VALUES (1, 'Marbella', 2, '12/12/2019');")

        self.connection.commit()

    def add_data(self):
        craft_id = input("Please enter the aircraft ID number for this flight ==> ")
        destination = str(input("Where are you flying to? "))
        duration = float(input("How many hours is this flight? "))

        return craft_id, destination, duration







test = Flight_Trip()
# test.create_table()
# test.existing_flights()
print(test.view_table())