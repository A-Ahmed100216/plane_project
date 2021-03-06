from people_class import People
from db_connection import DB_Connection

# Class for the Customers that inherits from People
class Customer(People):
   # initialise the class
    def __init__(self, passport_number, first_name, surname, tax_number):
        # inherit these variables from the people class
        super().__init__(passport_number, first_name, surname)
        self.tax_number = tax_number
        # connection instance to be used later,
        # rather than inherit from this class
        self.test = DB_Connection()

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

# used to ensure these tests only are done when calling from this file
if __name__ == "__main__":
    customer = Customer("68546354", "Harry", "Potter", "653214")
    customer.add_to_customer_table("68546354", "Harry", "Potter", "653214", "2", "Male", 0)
