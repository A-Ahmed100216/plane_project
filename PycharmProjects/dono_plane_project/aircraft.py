# Create an aircraft class and initialise
import pyodbc  #Import pyodbc so that you can connect to a database

# Create a class that connects to the database
class DB_Connection():
    def __init__(self):
        self.server = "databases1.spartaglobal.academy"
        self.database = "bada_airlines"  # the name of our newly created database
        self.username = "SA"
        self.password = "Passw0rd2018"
        # establish connection
        self.connection = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)

        self.cursor = self.connection.cursor()



# from connection import Connection
class Aircraft(DB_Connection):
    def __init__(self):
        super().__init__()
        #self.plane()
        #self.helicopter()
        self.fly=bool
        self.refuel=bool
        self.land=bool


    # Create methods for creating table
    def create_table(self):
        # Create a table in the database to store aircraft data
        crafts = self.cursor.execute("CREATE TABLE aircraft (craft_id INT NOT NULL IDENTITY(1,1) PRIMARY KEY, Type VARCHAR(20), Model VARCHAR(100), Capacity INT, Num_Classes INT, Terminal INT;")

    # # Create plane method for inserting plane data
    # def plane(self):
    #     self.cursor.execute(
    #         "INSERT INTO aircraft (Type, Model, Capacity, Num_Classes) VALUES ('plane', 'A380',517,3,1)")
    #     self.cursor.execute(
    #         "INSERT INTO aircraft (Type, Model, Capacity, Num_Classes) VALUES ('plane', 'B777',364,3,1)")
    #     self.cursor.execute(
    #         "INSERT INTO aircraft (Type, Model, Capacity, Num_Classes) VALUES ('plane', 'A320neo',160,2,2)")
    #     self.cursor.execute(
    #         "INSERT INTO aircraft (Type, Model, Capacity, Num_Classes) VALUES ('plane', '787 Dreamliner',254,2,1)")
    #     self.cursor.execute(
    #         "INSERT INTO aircraft (Type, Model, Capacity, Num_Classes) VALUES ('plane', 'A319',110,2,2)")
    #
    # # Create helicopter method for inserting helicopter data
    # def helicopter(self):
    #     self.cursor.execute(
    #         "INSERT INTO aircraft (Type, Model, Capacity, Num_Classes) VALUES ('helicopter', 'AS350 B2',5,0,3)")
    #
    #
    # # Define method for adding new data
    # def add_data(self):
    #     craft_type = input("Please enter the type of craft i.e helicopter or plane: ")
    #     model = input("Please enter the aircraft model: ")
    #     capacity = int(input("Please enter the craft capacity: "))
    #     travel_class=int(input("Please enter the class configuration: "))
    #     terminal = int(input("Please enter the terminal number: "))
    #     if craft_type!="helicopter" or "plane":
    #         print("invalid input. Please enter helicopter or plane")
    #         return craft_type
    #     self.cursor.execute(f"INSERT INTO aircraft (Type, Model, Capacity, Num_Classes) VALUES ('{craft_type}', '{model}',{capacity},{travel_class},{terminal})")


# Instantiate class
conn=DB_Connection()
test=Aircraft()
test.create_table()