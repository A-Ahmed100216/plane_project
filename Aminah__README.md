# Engineering 74: Plane Project

# User Stories
1. As an airport assistant, I want to be able to create a passenger with name AND passport number so I can add them to the flight.
2. As an airport assistant, I want to be able to create flight_trip with a specific destination. 
3. As an airport assistant, I want to be able to assign and/or change a plane to my flight_trip, input my password so I can handle the problem.
4. As an airport assistant, I want to be able to add passengers to flight_trip so that I can sell tickets to them.
5. As an airport assistant, I want to be able to generate a flight_attendees list with passenger names and passport numbers so I can check their identity. 

# TASK - Create a class for aircraft 
 
* Import relevant modules 
```python
import pyodbc  #Import pyodbc so that you can connect to a database
import pandas as pd
```

* The aircraft class will be a child of the Connection class therefore enabling it to connect to the database. The Connection class is as follows:
```python
class DB_Connection:
    def __init__(self):
        self.server = "databases1.spartaglobal.academy"
        self.database = "bada_airlines"  # the name of our newly created database
        self.username = "SA"
        self.password = "Passw0rd2018"
        # establish connection
        self.connection = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        self.cursor = self.connection.cursor()
```
 
* The aircraft class will be used to define methods for inserting and adding data pertaining to aircraft:
    * type - is a plane or helicopter?
    * model - the type of plane or helicopter i.e A380, B777 etc.
    * capacity - what is the capacity of the aircraft
    * number of classes - this refers to the class configuration i.e. first/business/economy or economy/business.
    * terminal - the terminal the craft is located at.
* The class is initialised with aircraft attributes such as fly, refuel and land. These are set to booleans and will be defined in child classes.
* Following ths, methods are established to create a table in the "bada_airlines" database, insert data, view the data in the table, and add new data.

 ```python
# Create an aircraft class and initialise
class Aircraft(DB_Connection):
    def __init__(self):
        super().__init__()
        self.fly=bool
        self.refuel=bool
        self.land=bool


    # Create methods for creating table
    def create_table(self):
        # Create a table in the database to store aircraft data
        crafts = self.cursor.execute("CREATE TABLE aircraft (craft_id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,Type VARCHAR(20), Model VARCHAR(100), Capacity INT, Num_Classes INT, Terminal INT);")
        # Commit changes to database
        self.connection.commit()
        return crafts


    # Create plane method for inserting plane data
    def plane(self):
        self.cursor.execute(
            "INSERT INTO aircraft (Type, Model, Capacity, Num_Classes,Terminal) VALUES ('plane', 'A380',517,3,1)")
        self.cursor.execute(
            "INSERT INTO aircraft (Type, Model, Capacity, Num_Classes,Terminal) VALUES ('plane', 'B777',364,3,1)")
        self.cursor.execute(
            "INSERT INTO aircraft (Type, Model, Capacity, Num_Classes,Terminal) VALUES ('plane', 'A320neo',160,2,2)")
        self.cursor.execute(
            "INSERT INTO aircraft (Type, Model, Capacity, Num_Classes,Terminal) VALUES ('plane', '787 Dreamliner',254,2,1)")
        self.cursor.execute(
            "INSERT INTO aircraft (Type, Model, Capacity, Num_Classes,Terminal) VALUES ('plane', 'A319',110,2,2)")
        self.connection.commit()


    # Create helicopter method for inserting helicopter data
    def helicopter(self):
        self.cursor.execute(
            "INSERT INTO aircraft (Type, Model, Capacity, Num_Classes,Terminal) VALUES ('helicopter', 'AS350 B2',5,0,3)")
        self.connection.commit()

    # Method for viewing the data in the table
    def show_table(self):
        aircraft_table=self.cursor.execute("SELECT * FROM aircraft").fetchall()
        return aircraft_table

    # Define method for adding new data
    def add_data(self):
        craft_type = input("Please enter the type of craft i.e helicopter or plane: ")
        # if craft_type!="helicopter" or craft_type!="plane":
        #     print("invalid input. Please enter helicopter or plane")
        #     return craft_type
        model = input("Please enter the aircraft model: ")
        try:
            capacity = int(input("Please enter the craft capacity: "))
            travel_class=int(input("Please enter the class configuration: "))
            terminal = int(input("Please enter the terminal number: "))
        except ValueError as err:
            print("Please enter a number")
            return
        finally:
            pass

        self.cursor.execute(f"INSERT INTO aircraft (Type, Model, Capacity, Num_Classes,Terminal) VALUES ('{craft_type}', '{model}',{capacity},{travel_class},{terminal})")
        # self.connection.commit()


class Query(DB_Connection):

    def sql_query(self):
        query = input("Please enter your sql query    ")
        exported_data = pd.read_sql_query(f'{query}', self.connection)
        df_2 = pd.DataFrame(exported_data)
        print(df_2)


# Instantiate class
test=Aircraft()
# test.create_table()
# test.plane()
# test.helicopter()
test.add_data()
print(test.show_table())

#
# query=Query()
# query.sql_query()





```

