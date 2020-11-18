import pyodbc
import pandas as pd

server = 'databases1.spartaglobal.academy'
database = 'bada_airlines'
username = 'SA'
password = 'Passw0rd2018'
driver = '{ODBC Driver 17 for SQL Server}'

conn = pyodbc.connect(
    'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = conn.cursor()


def sql_query():
    query = input("Please enter your sql query    ")
    exported_data = pd.read_sql_query(f'{query}', conn)
    df_2 = pd.DataFrame(exported_data)
    print(df_2)


sql_query()
