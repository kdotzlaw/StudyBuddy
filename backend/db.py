'''
Defines helper functions used in API calls using pyodbc (for database connections)
and SQL prepared statements
'''
import pyodbc

# connection information can change as we include security

conn = (r'Driver=ODBC Driver 18 for SQL Server;'
        r'Server=localhost;'
        r'Database=StudyBuddy;'
        r'Trusted_Connection=Yes'
        )
cnxn = pyodbc.connect(conn)
cursor = cnxn.cursor()

'''
PRECONDITION: passed string <username> which will be used to find the user in the db
POSTCONDITION: if the user with <username> exists in the database, return their information (form of string)
'''
def getUser(name):
    result = cursor.execute("SELECT * FROM Users WHERE username = ?", name).fetchone()
    return result


'''
PRECONDITION: account creation requested, need to add a new entry to users table
POSTCONDITION: account has been created and added to users table with given information
'''


def createAccount(username, password):
    # cursor.execute("INSERT INTO Users (username, password) VALUES (?, ?)",username, password)
    prep_stmt = "INSERT INTO Users (username, password) VALUES (?,?)"
    cursor.execute(prep_stmt, username, password)


# for testing
def removeUser(username):
    cursor.execute("DELETE FROM Users WHERE username = ?", username)


def getAllUsers():
    temp = cursor.execute("SELECT * FROM Users")
    for [uID, username, password, user_email, xp] in temp:
        result = str(uID) + " " + str(username) + " " + str(password) + " " + str(user_email) + " " + str(xp)
    return result
