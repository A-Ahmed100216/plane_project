# Create an aircraft class and initialise
import pyodbc

# from connection import Connection
class Aircraft(Connection):
    def __init__(self):
        self.plane()
        self.helicopter()


# Create methods for helicopter and plane
    def plane(self):
        craft_type=["A380","B777","A320neo"]
        capacity=[517,364,160]
        travel_class =[3,3,2]

    def helicopter(self):
        pass

    def create_table(self):
        # Create a table in the database to store aircraft data
        crafts=self.cursor.execute("CREATE TABLE aircraft (craft_id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,Type VARCHAR(20), Model VARCHAR(55), Capacity INT, Num_Classes INT ")

    def insert_data(self):
        # Insert data into the crafts table
        self.cursor.execute(
            f"INSERT INTO aircraft (Type, Model, Capacity, Num_Classes) VALUES ('plane', '{craft_type[0]}','{capacity[0]}','{travel_class[0]}')")





# Create tables in sql
