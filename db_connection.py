#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 Amaan Hashmi-Ubhi <AmaanHUB@gmail.com>
#
# Distributed under terms of the MIT license.

import pyodbc  # Import pyodbc so that you can connect to a database

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

# create and instance of this class to test the connection
if __name__ == "__main__":
    test = DB_Connection()
    test.__init__()

