'''
Defines helper functions used in API calls using pyodbc (for database connections)
and SQL prepared statements
'''
import pyodbc
#connection information can change as we include security

conn = (r'Driver=SQL Server;'
        r'Server=(local);'
        r'Database=StudyBuddy;'
        r'Trusted_Connection=yes'
        )
cnxn = pyodbc.connect(conn)
cursor = cnxn.cursor()

'''
PRECONDITION: passed string <username> which will be used to find the user in the db
POSTCONDITION: if the user with <username> exists in the database, return their information (form of table entry)
'''
def getUser(username):
    result = cursor.execute("SELECT * FROM Users WHERE username = ?", username)
    return result.fetchall()
'''
PRECONDITION: account creation requested, need to add a new entry to users table
POSTCONDITION: account has been created and added to users table with given information
'''
def createAccount(username, password):
    cursor.execute("INSERT INTO Users (username = ?, password = ?)", username, password)


