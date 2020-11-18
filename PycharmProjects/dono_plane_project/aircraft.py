# Create an aircraft class and initialise
import pyodbc  #Import pyodbc so that you can connect to a database
import pandas as pd
# Create a class that connects to the database
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
        # self.connection.commit()
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



    def show_table(self):
        aircraft_table=self.cursor.execute("SELECT * FROM aircraft").fetchall()
        return aircraft_table

    # Define method for adding new data
    def add_data(self):
        craft_type = input("Please enter the type of craft i.e helicopter or plane: ")
        while craft_type=="helicopter" or craft_type=="plane":
            break
        else:
            print("Invalid, please enter helicopter or plane")
            return craft_type


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



if __name__ =="__main__":
    # Instantiate class
    test=Aircraft()
    print(test.show_table())
    # test.create_table()
    # test.plane()
    # test.helicopter()
    # test.add_data()
    # print(test.show_table())

    #
    # query=Query()
    # query.sql_query()