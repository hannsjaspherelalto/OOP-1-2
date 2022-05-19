import pyodbc

try:
    connect = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};'
                             r'DBQ=C:\Users\Jaspher\Documents\Recit.accdb;')
    print("Connected")


except pyodbc.Error:
    print("Error")