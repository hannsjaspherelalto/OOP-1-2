import pyodbc

try:
    connect = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};'
                             r'DBQ=C:\Users\Jaspher\Documents\Recit.accdb;')
    print("Connected")

    user_id = 11
    database = connect.cursor()
    database.execute('delete from Database01 where id = ?', (user_id))
    database.commit()
    print('Deleted')



except pyodbc.Error:
    print("Error")
