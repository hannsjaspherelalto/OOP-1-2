import pyodbc

try:
    connect = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};'
                             r'DBQ=C:\Users\Jaspher\Documents\Recit.accdb;')
    print("Connected")

    database = connect.cursor()
    database.execute('SELECT * FROM Database01')

    for x in database.fetchall():
        print(x)

except pyodbc.Error:
    print("Error")