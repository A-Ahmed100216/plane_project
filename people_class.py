#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

# import Connection from the connection class that Donovan is
# making
from connection_class import Connection

# create a People class. Superclass of Passengers and Staff


class People:
    # initialise the class with variable
    def __init__(self, tax_number, first_name, surname):
        self.tax_number = tax_number
        self.first_name = first_name
        self.surname = surname

    # function to create a table within the database for passengers
    def create_customer_table(self):
        if self.cursor.tables(table="Customer", tableType="TABLE").fetchone():
            # stop the function and print message if table is already created
            print("Passengers table is already created")
        else:
            # create the tables
            self.cursor.execute("""CREATE TABLE Customer(
                                PassportID VARCHAR(20) NOT NULL IDENTITY PRIMARY KEY,
                                FirstName VARCHAR(MAX) NOT NULL,
                                Surname VARCHAR(MAX) NOT NULL,
                                FlightID INT NOT NULL REFERENCES Flight_Trip(FlightID),
                                Gender VARCHAR(10),
                                Boarded_Flight BOOLEAN
                                );""")

    # function to create a table within the database for the staff
    def create_employee_table(self):
        if self.cursor.tables(table="Employee", tableType="TABLE").fetchone():
            # stop the function and print message if table is already created
            print("Employee table is already created")
        else:
            self.cursor.execute("""CREATE TABLE Staff(
                                    StaffPassportID VARCHAR(20) NOT NULL IDENTITY PRIMARY KEY,
                                    FirstName VARCHAR(MAX) NOT NULL,
                                    Surname VARCHAR(MAX) NOT NULL,
                                    FlightID INT NOT NULL REFERENCES Flight_Trip(FlightID),
                                    Gender VARCHAR(10),
                                    Occupation VARCHAR(20)
                                    );""")
# only do these tests if running from this file
if __name__ == "__main__":
    testing = People("1235876584NP", "Chicken", "Little")
    print(testing.tax_number)
    print(testing.first_name)
    print(testing.surname)
