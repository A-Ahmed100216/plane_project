# Engineering 74: Plane Project

 # Plane Project
## Requirements
* To access database one needs to install the `pyodbc` module
```sh
pip install pyodbc
```
## Setting Up Microsoft SQL Server In Docker

* First ensure docker is running on the server/local machine that you are using. If you have a systemd based machine you can use:
`sudo systemctl status docker.service`

* Download the relevant docker image of MSSQL
`sudo docker pull mcr.microsoft.com/mssql/server`

* Start the docker container
```
sudo docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=<YourStrong@Passw0rd>" \
   -p 1433:1433 --name <name_of_choice> -h <probably_the_same_name> \
   -d mcr.microsoft.com/mssql/server
 ```

* View if the container is running
`sudo docker ps -a`


* Change the password (or keep the same) that you previously gave with the following command, as it will prevent anyone with access to the container from seeing the SA password that you have previously chosen
```
sudo docker exec -it <name_of_choice> /opt/mssql-tools/bin/sqlcmd \
   -S localhost -U SA -P "<YourStrong@Passw0rd>" \
   -Q 'ALTER LOGIN SA WITH PASSWORD="<YourNewStrong@Passw0rd>"'
```

* To connect to the SQL server inside the container, one has to access the container with
` sudo docker exec -it <name_of_choice> "bash"`

* To access the actual SQL server itself run
`/opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P "<YourNewStrong@Passw0rd>"`

* Tah-dah, now you are now on your SQL database! One small difference than running from Azure Data Studio or the like is that you need to input `GO` after each of your commands (preferably after you have pressed enter) .e.g.
```sql
CREATE DATABASE chickens

GO
```

* This isn't the end of the road though, if you want people to be able to access this SQL server, you need to allow network access to this. Firstly, you need to map the SQL Server to a port on the actual computer (likely the same one you chose before, 1433). **Note, you need the SQL Server command-line tools installed on the device that is hosting the docker container before you can do this**
`sqlcmd -S <ip_address>,1433 -U SA -P "<YourNewStrong@Passw0rd>"`

* Finally, you need to remember to open up this port in your firewall and enable port forwarding for this device and for this port on your router (very variable so no examples here)

* Now people should be able to access the databases that you create, though you may want to create separate users within this, so that they can only access what you want them to

* For more information on docker with MSSQL, see the links below
	* ![Microsoft Documentation](https://docs.microsoft.com/en-gb/sql/linux/quickstart-install-connect-docker?view=sql-server-ver15&pivots=cs1-bash)

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

* **Note, the `Flight_Trip` table must have been created before these functions to create these tables are called, due to them referencing this table**

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

* Create some tests in an `if __name__ == "__main__"` statement so that they only run when this file is being called directly
```python
    # initialise an object for testing
    testing = People("1235876910", "Chicken", "Little")
    # print out various attributes to make sure that it has
    # been properly initialised
    print(testing.passport_number)
    print(testing.first_name)
    print(testing.surname)
    # test the creation of tables functions
    testing.create_customer_table()
    testing.create_employee_table()
```

## Customers Class

* First import the `People` and `DB_Connection` classes
```python
from people_class import People
from db_connection import DB_Connection
```
* Create the class `Customer` that inherits from `People`
```python
# Class for the Customers that inherits from People
class Customer(People):
```

* Declare the variables in the constructor (.i.e. `__init__` method)
```python
    # initialise the class
    def __init__(self, passport_number, first_name, surname, tax_number):
        # inherit these variables from the people class
        super().__init__(passport_number, first_name, surname)
        self.tax_number = tax_number
        # connection instance to be used later,
        # rather than inherit from this class
        self.test = DB_Connection()
```

* A relatively simple function to add a user to the `Customers` table is seen below. It takes all the attributes within the function call, so that the user can be asked for input within the `user_interface` file further down the road, which is then piped into this function
```python
    # Add data to the Customer table using INSERT
    def add_to_customer_table(self, passport_number, first_name, surname,tax_number, flight_id, gender, boarded_flight):
        # check if the table is created
        if self.test.cursor.tables(table="Customers", tableType="TABLE").fetchone():
            # do the SQL INSERT queries
            self.test.connection.execute(f"""INSERT INTO Customers(
                                        PassportID,TaxNumber,FirstName,Surname,Flight_ID,Gender,Boarded_Flight
                                        ) VALUES (
                                        '{passport_number}','{tax_number}','{first_name}','{surname}',{flight_id},
                                        '{gender}', {boarded_flight});""")
            # commit the SQL statement to the database
            self.test.connection.commit()
        else:
            # a message to inform the user what is going on
            print("Customers table does not exist, please try again")
```

* A function to show all the current customers utilises a simple `SELECT * FROM <table_name>` statement with a for loop to output the results
```python
    # function to show all the customers
    def show_customers(self):
        # check if the table is created
        if self.test.cursor.tables(table="Customers", tableType="TABLE").fetchone():
            customers = self.test.cursor.execute("""SELECT * FROM Customers""")
            # for loop to print all the rows of customers
            for rows in customers:
                print(rows)
        else:
            # a message to inform the user what is going on
            print("Customers table does not exist, please try again")
```

* Again, tests are done at the end of the file to ensure things are running smoothly
```python
# used to ensure these tests only are done when calling from this file
if __name__ == "__main__":
    customer = Customer("68546354", "Harry", "Potter", "653214")
    customer.add_to_customer_table("68546354", "Harry", "Potter", "653214", "2", "Male", 0)
```


## Employee Class

* Import from the relevant libraries and classes (the same ones as in the `Customer` class)
```python
# import from the relevant files
from people_class import People
from db_connection import DB_Connection
```

* Create the `Employee` class that inherits from `People`
```python
# create the class that inherits from People
class Employees(People):
```

* Initialise the class and the attributes
```python
    # initialise the class
    def __init__(self, passport_number, first_name, surname, gender, occupation):
        # inherit these variables from the People class
        super().__init__(passport_number, first_name, surname)
        self.gender = gender
        self.occupation = occupation
        # connection instance to be used later
        self.test = DB_Connection()
```

* A function to add an employee to the `Employee` table. Functionally similar to the `add_to_customer_table` function in `Customer`
```python
    # Add data to the Customer table using INSERT
    def add_to_employees_table(self, passport_number, first_name, surname,
                               gender, occupation, flight_id):
        # check if the table is created
        if self.test.cursor.tables(table="Employees", tableType="TABLE").fetchone():
            # do the SQL INSERT queries
            self.test.connection.execute(f"""INSERT INTO Employees(
                                        StaffPassportID,FirstName,Surname,Flight_ID,Gender,Occupation
                                        ) VALUES (
                                        '{passport_number}','{first_name}','{surname}','{flight_id}',
                                        '{gender}', '{occupation}'
                                      );""")
            self.test.connection.commit()
        else:
            # message to show user if table does not exist
            print("Employees table does not exist, please try again")
```

* A function to show all employees, again, functionally similar to the customer variant
```python
    # function to show all the employees in records
    def show_all_employees(self):
        # check if the table has been created
        if self.test.cursor.tables(table="Employees", tableType="TABLE").fetchone():
            employees = self.test.connection.execute("""SELECT * FROM Employees""").fetchall()
            # for loop to print all thw records in the table
            for rows in employees:
                print(rows)
        else:
            # message to show user if table does not exist
            print("Employees table does not exist, please try again")
```

* Finally, some tests are made on an instantiated object of this class, again in such a way that they will only work when this file is being called directly
```python
# testing below this so that they are only run when this file is directly being run
if __name__ == "__main__":
    # instantiate an object and test all the functions
    employees = Employees("102901092", "Chicken", "Little", "Male", "Pilot")
    employees.add_to_employees_table("102901092", "Chicken", "Little", "Male", "Pilot", "1")
    employees.show_all_employees()
```
