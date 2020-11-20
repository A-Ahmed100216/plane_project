# This README Takes You Through The Tasks Assigned to Donovan

### Create Class that Connects to the Database
* Step 1:
    - import pyodbc to use method that connects to DB
    
    ```import pyodbc ```
    
* Step 2:
    - Create a class that holds attributes with the details of the DB
```
class DB_Connection():
    def __init__(self):
        self.server = "hashimoto.duckdns.org"
        self.database = "bada_airlines"  # the name of our newly created database
        self.username = "**"
        self.password = "*****"
```

* Step 3:
    - Establish a connection with the driver
```
self.connection = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
```

* Step 4:
    - Create a cursor in order to interact with the DB
```
self.cursor = self.connection.cursor()
```

* Step 5:
    - Run some tests in order to see if the connection has been made
```
if __name__ =="__main__":
    test = DB_Connection()
    test.__init__()
```

### Create a Flight Trip Class
* Step 1:
    - Import the DB_Connection Class from the relevant file
```
from db_connection_class import DB_Connection
```

* Step 2:
    - Create a class called Flight_Trip
    - Inherit from the DB_Connection class
```
class Flight_Trip(DB_Connection):
    def __init__(self):
        super().__init__()
```

* Step 3:
 
**Create methods in the class too...**
* Create table
```
    def create_table(self):
        self.cursor.execute("CREATE TABLE Flight_Trip (Flight_ID INT NOT NULL IDENTITY(1,1) PRIMARY KEY, craft_id INT, Destination VARCHAR(100), Duration_hrs INT, Date VARCHAR(100), Time VARCHAR(100));")
```
* View table
```
  def view_table(self):
        flights_table = self.cursor.execute("SELECT * FROM Flight_Trip").fetchall() # fetches all the info in the table
        return flights_table
```
* Add existing data into the table
```
 def existing_flights(self):
        self.cursor.execute("INSERT INTO Flight_Trip (craft_id, Destination, Duration_hrs, Date, Time) VALUES (1, 'Marbella', 2, '12/12/2019', '12:00');")
        self.cursor.execute(
            "INSERT INTO Flight_Trip (craft_id, Destination, Duration_hrs, Date, Time) VALUES (2, 'St Lucia', 8, '14/12/2019', '01:00');")
        self.cursor.execute(
```
* Enable the user to input data
```
    def add_flight(self):
        # Assign the user input to the relevant variables
        craft_id = input("Please enter the aircraft ID number for this flight ==> ")
        destination = str(input("Where are you flying to? "))
        duration = int(input("How many hours is this flight? "))
        date = str(input("Please enter the date of this flight(dd/mm/yyyy) ==> "))
        time = str(input("What time is the flight?(hh:mm) "))

        # insert these newly assigned variables into the DB table
        self.cursor.execute(f"INSERT INTO Flight_Trip (craft_id, Destination, Duration_hrs, Scheduled_Date, Scheduled_Time) VALUES ('{craft_id}', '{destination}', '{duration}', '{date}', '{time}');")

        self.connection.commit()
```
* Test your code
```
if __name__=="__main__":
    test = Flight_Trip()
    test.create_table()
    test.existing_flights()
    test.add_flight()
    print(test.view_table())
```
    
    