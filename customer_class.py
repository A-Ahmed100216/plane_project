#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

# import class
from people_class import People

from db_connection_class import DB_Connection
# Class for the Customers


class Customer(People):
    def __init__(self, passport_number, first_name, surname, tax_number):
        super().__init__(passport_number, first_name, surname)
        self.tax_number = tax_number

        # connection instance to be used later
        self.test = DB_Connection()

    # Add data to the Customer table using INSERT
    def add_to_customer_table(self, passport_number, first_name, surname,

                              tax_number, flight_id, gender, boarded_flight):
        # check if the table is created
        if self.test.cursor.tables(table="Customers", tableType="TABLE").fetchone():
            # do the SQL INSERT queries
            self.test.connection.execute(f"""INSERT INTO Customers(
                                        PassportID,TaxNumber,FirstName,Surname,FlightID,Gender,Boarded_Flight
                                        ) VALUES (
                                        {passport_number},{tax_number},{first_name},{surname},{flight_id},
                                        {gender}, {boarded_flight}
                                      );""")
            self.test.connection.commit()
        else:
            print("Customers table does not exist, please try again")

    # function to show all the customers
    def show_customers(self):
        if self.test.cursor.tables(table="Customers", tableType="TABLE").fetchone():
            customers = self.test.cursor.execute("""SELECT * FROM Customers""")
            # for loop to print all the rows of customers
            for rows in customers:
                print(rows)
        else:
            print("Customers table does not exist, please try again")


if __name__ == "__main__":
    customer = Customer("68546354", "chicken", "little", "6532168354")
    customer.add_to_customer_table("iauhrdsfd", "seoufnse", "Chicken1", "Little1", "0", "NB", 0)
