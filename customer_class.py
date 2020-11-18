#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

# import class
from people_class import People

from db_connection_class import DB_Connection
# Class for the Customers


class Customer(People):
    def __init__(self, passport_number, first_name, surname, tax_number,
                 number_of_adults, number_of_children, number_of_infants):
        super().__init__(passport_number, first_name, surname)
        self.tax_number = tax_number
        self.number_of_adults = number_of_adults
        self.number_of_children = number_of_children
        self.number_of_infants = number_of_infants
        # connection instance to be used later
        self.test = DB_Connection()

    # Add data to the Customer table using INSERT
    def add_to_customer_table(self, passport_number, first_name, surname,
                              tax_number):
        # check if the table is created
        if self.test.cursor.tables(table="Customer", tableType="TABLE").fetchone():
            # do the SQL INSERT queries
            self.test.connection.execute("""INSERT INTO Customer(
                                        PassportID,TaxNumber,FirstName,Surname,FlightID,Gender,Boarded_Flight
                                        ) VALUES (
                                        {passport_number},{tax_number},{first_name},{surname}
                                      );""")
            self.test.connection.commit()
        else:
            print("Customer table does not exist, please try again")
        # add section here to get and add number_of_infants etc to the Booking

    def number_of_infants(self):
        return self.number_of_infants

    def number_of_children(self):
        return self.number_of_children

    def number_of_adults(self):
        return self.number_of_adults


if __name__ == "__main__":
    customer = Customer("68546354", "chicken", "little", "6532168354", 23, 1, 0, 0)
    print(customer.age)
    customer.add_to_customer_table("iauhrdsfd", "seoufnse", "Chicken1", "Little1", 5, "A", 0)