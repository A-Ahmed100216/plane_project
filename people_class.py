#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

# create a People class. Superclass of Passengers and Staff


class People:
    # initialise the class with variable
    def __init__(self, tax_number, first_name, surname):
        self.tax_number = tax_number
        self.first_name = first_name
        self.surname = surname


# only do these tests if running from this file
if __name__ == "__main__":
    testing = People("1235876584NP", "Chicken", "Little")
    print(testing.tax_number)
    print(testing.first_name)
    print(testing.surname)
