# Import the DB_Connection class form the correct file
from db_connection_class import DB_Connection

# Create a class that inherits from the DB connection (Parent)
class Flight_Trip(DB_Connection):
    def __init__(self):
        super().__init__() # takes on the attributes within the Parent class

# Now create a function that creates a table for the flight trip data
    def create_table(self):
        self.cursor.execute("CREATE TABLE Flight_Trip (Flight_ID INT NOT NULL IDENTITY(1,1) PRIMARY KEY, craft_id INT, Destination VARCHAR(100), Duration_hrs INT, Date VARCHAR(100), Time VARCHAR(100));")
    # self.cursor is taken from the parent class (DB_Connection)

    # Create a function that allows the user to view the table
    def view_table(self):
        flights_table = self.cursor.execute("SELECT * FROM Flight_Trip").fetchall() # fetches all the info in the table
        return flights_table

    # Insert some existing data into the flight trip table
    def existing_flights(self):
        self.cursor.execute("INSERT INTO Flight_Trip (craft_id, Destination, Duration_hrs, Date, Time) VALUES (1, 'Marbella', 2, '12/12/2019', '12:00');")
        self.cursor.execute(
            "INSERT INTO Flight_Trip (craft_id, Destination, Duration_hrs, Date, Time) VALUES (2, 'St Lucia', 8, '14/12/2019', '01:00');")
        self.cursor.execute(
            "INSERT INTO Flight_Trip (craft_id, Destination, Duration_hrs, Date, Time) VALUES (4, 'Los Angeles', 10, '14/05/2019', '08:00');")
        self.cursor.execute(
            "INSERT INTO Flight_Trip (craft_id, Destination, Duration_hrs, Date, Time) VALUES (3, 'Antigua', 9, '06/06/2019', '10:00');")

        self.connection.commit() # commit saves the changes made to the DB table

    # Create a function that allows the user to insert data into the Flight_Trip table
    def add_flight(self):
        # Assign the user input to the relevant variables
        craft_id = input("Please enter the aircraft ID number for this flight ==> ")
        destination = str(input("Where are you flying to? "))
        duration = int(input("How many hours is this flight? "))
        date = str(input("Please enter the date of this flight(dd/mm/yyy) ==> "))
        time = str(input("What time is the flight?(hh:mm) "))

        # insert these newly assigned variables into the DB table
        self.cursor.execute(f"INSERT INTO Flight_Trip (craft_id, Destination, Duration_hrs, Date, Time) VALUES ('{craft_id}', '{destination}', '{duration}', '{date}', '{time}');")

        self.connection.commit()






# Run some tests to see if the code is working
if __name__=="__main__":
    test = Flight_Trip()
    # test.create_table()
    # test.existing_flights()
    test.add_flight()
    # print(test.view_table())