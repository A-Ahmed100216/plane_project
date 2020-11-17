#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

# import class
from people_class import People

# Class for the Customers


class Customer(People):
    def __init__(self, passport_number, first_name, surname, tax_number,
                 number_of_adults, number_of_children, number_of_infants):
        super().__init__(passport_number, first_name, surname)
        self.tax_number = tax_number
        self.number_of_adults = number_of_adults
        self.number_of_children = number_of_children
        self.number_of_infants = number_of_infants


    # Add data to the
    def add_to_customer_table(self, passport_number, first_name, surname,
                              tax_number):
        pass

    def number_of_infants(self):
        return self.number_of_infants

    def number_of_children(self):
        return self.number_of_children

    def number_of_adults(self):
        return self.number_of_adults



if __name__ == "__main__":
    customer = Customer("68546354", "chicken", "little", "6532168354", 23, 1, 0, 0)
    print(customer.age)

