#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

# import Connection from the connection class that D made
from db_connection_class import DB_Connection

# create a People class. Superclass of Passengers and Staff


class People:
    # initialise the class with variable
    def __init__(self, passport_number, first_name, surname):
        self.passport_number = passport_number
        self.first_name = first_name
        self.surname = surname

    # function to create a table within the database for passengers
    def create_customer_table(self):
        if self.cursor.tables(table="Customer", tableType="TABLE").fetchone():
            # stop the function and print message if table is already created
            print("Customers table is already created")
        else:
            # create the tables
            print("Creating customer table \n")
            self.cursor.execute("""CREATE TABLE Customer(
                                PassportID VARCHAR(20) NOT NULL IDENTITY PRIMARY KEY,
                                TaxNumber VARCHAR(20) NOT NULL,
                                FirstName VARCHAR(MAX) NOT NULL,
                                Surname VARCHAR(MAX) NOT NULL,
                                FlightID INT NOT NULL REFERENCES Flight_Trip(FlightID),
                                Gender VARCHAR(10),
                                Boarded_Flight BOOLEAN
                                );""")
            self.cursor.commit()

    # function to create a table within the database for the staff
    def create_employee_table(self):
        if self.cursor.tables(table="Employee", tableType="TABLE").fetchone():
            # stop the function and print message if table is already created
            print("Employee table is already created")
        else:
            print("Creating employee table \n")
            self.cursor.execute("""CREATE TABLE Staff(
                                    StaffPassportID VARCHAR(20) NOT NULL IDENTITY PRIMARY KEY,
                                    FirstName VARCHAR(MAX) NOT NULL,
                                    Surname VARCHAR(MAX) NOT NULL,
                                    FlightID INT NOT NULL REFERENCES Flight_Trip(FlightID),
                                    Gender VARCHAR(10),
                                    Occupation VARCHAR(20)
                                    );""")
            self.cursor.commit()


# only do these tests if running from this file
if __name__ == "__main__":
    testing = People("1235876584NP", "Chicken", "Little")
    print(testing.passport_number)
    print(testing.first_name)
    print(testing.surname)
    testing.create_employee_table()
    testing.create_customer_table()