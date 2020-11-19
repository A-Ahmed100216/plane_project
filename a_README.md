# Engineering 74: Plane Project

 # Plane Project
## Requirements
* To access database one needs to install the `pyodbc` module
```sh
pip install pyodbc
```

## People Class

* Import the class to enable connection to the database
```python
# import Connection from the connection class that D made
from db_connection_class import DB_Connection
```

* Create a class for People, and initiate it with the `tax_number`, `first_name`, and `surname` variables
```python
# create a People class. Superclass of Passengers and Staff


class People:
    # initialise the class with variable
    def __init__(self, passport_number, first_name, surname):
        self.passport_number = passport_number
        self.first_name = first_name
        self.surname = surname
```

* Create a function to create the actual table to hold the customers, with a check if the table has already been made (and prints a message if has), otherwise creates the table
```python
    # function to create a table within the database for passengers
    def create_customer_table(self):
        if self.cursor.tables(table="Customer", tableType="TABLE").fetchone():
            # stop the function and print message if table is already created
            print("Customers table is already created")
        else:
            # create the tables
            self.cursor.execute("""CREATE TABLE Customer(
                                PassportID VARCHAR(20) NOT NULL IDENTITY PRIMARY KEY,
								TaxNumber VARCHAR(20) NOT NULL,
                                FirstName VARCHAR(MAX) NOT NULL,
                                Surname VARCHAR(MAX) NOT NULL,
                                FlightID INT NOT NULL REFERENCES Flight_Trip(FlightID),
                                Gender VARCHAR(10),
                                Boarded_Flight BOOLEAN
                                );""")

```

* Create a function to create the Employee table, with the same constraints
```python
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
```

* Create some tests in an `if __name__ == "__main__"` statement so that they only run when this file is being created
	;kjadshfv
