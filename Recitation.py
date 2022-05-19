import pyodbc

try:
    connect = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Jaspher\Downloads\Database01.accdb;')
    print("Connected")

    database = connect.cursor()
    database.commit()
    database.execute('''
                        INSERT INTO Table1 (ID, FullName, Age, Address, Birthdate, SemGrade)
                        VALUES (?,?,?,?,?,?)''', (11, 'Hanns Elalto', 20, 'Cavite', '25/04/2002', 90))
    print("Updated")

except pyodbc.Error:
    print("Error")