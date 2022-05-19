import pyodbc

try:
    connect = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};'
                             r'DBQ=C:\Users\Jaspher\Documents\Recit.accdb;')
    print("Connected")

    database = connect.cursor()
    database.execute(''' INSERT INTO Database01 (ID, Student Name, Age, Address, Birthday, SemGrades)
                     VALUES ('11', 'Hanns', '20', 'Cavite', '04/25/2002', '100') ''')
    database.commit()
    print("Updated")

except pyodbc.Error:
    print("Error")