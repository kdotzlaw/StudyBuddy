import pyodbc

def getUser(name):
    conn = (r'Driver=SQL Server;'
            r'Server=(local);'
            r'Database=StudyBuddy;'
            r'Trusted_Connection=yes'
            )
    cnxn = pyodbc.connect(conn)
    cursor = cnxn.cursor()
    result = cursor.execute("SELECT * FROM Users WHERE username = ?", name).fetchall()
    if not result:
        cnxn.close()
        return None
    cnxn.close()
    return result[0]


def getClasses(username):
    conn = (r'Driver=SQL Server;'
            r'Server=(local);'
            r'Database=StudyBuddy;'
            r'Trusted_Connection=yes'
            )
    cnxn = pyodbc.connect(conn)
    cursor = cnxn.cursor()
    user = getUser(username)
    if not user:
        cnxn.close()
        return None
    # get user id
    userID = user.uID
    record = cursor.execute("SELECT * FROM Classes WHERE FK_uID = ? AND is_complete = 0;", userID).fetchall()
    if not userID or not record:
        cnxn.close()
        return None
    cnxn.close()
    return record