import pyodbc

try:
    connect = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};'
                             r'DBQ=C:\Users\Jaspher\Documents\Recit.accdb;')
    print("Connected")

    user_id = 7
    Address = 'Cavite'
    database = connect.cursor()
    database.execute(' update Database01 set Address = ? where id = ?', (Address, user_id))
    database.commit()
    print('Updated')



except pyodbc.Error:
    print("Error")
