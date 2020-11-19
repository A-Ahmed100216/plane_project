from aircraft_class import DB_Connection
import hashlib

class Admin(DB_Connection):
    # def __init__(self):



    def create_user_login(self):
        firstname=input("Please enter your first name: ")
        lastname=input("Please enter your last name: ")
        username=input("Please enter a username: ")
        password=input("Please enter a password: ")
        result = hashlib.md5(password.encode()).hexdigest()
        self.cursor.execute(f"INSERT INTO admin(First_Name,Last_Name,Username,Password) VALUES('{firstname}','{lastname}','{username}','{result}')")
        self.connection.commit()





test=Admin()
test.create_user_login()