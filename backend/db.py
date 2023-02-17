'''
Defines helper functions used in API calls using pyodbc (for database connections)
and SQL prepared statements
'''
import pyodbc

# connection information can change as we include security
# PROD CONNECTION STRING
'''conn = (r'Driver=ODBC Driver 17 for SQL Server;'
        r'Server=localhost;'
        r'Database=StudyBuddy;'
        r'UID=sa;'
        r'PWD=dbtools.IO'
        )'''
# DEV CONNECTION STRING - D.N.T
conn = (r'Driver=SQL Server;'
        r'Server=(local);'
        r'Database=StudyBuddy;'
        r'Trusted_Connection=yes'
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
    prep_stmt = "INSERT INTO Users (username, password) VALUES (?,?);"
    cursor.execute(prep_stmt, username, password)
''' 
PRECONDITION: all users are present in the db
POSTCONDITION: user with 'username' has been removed from the db
'''
def removeUser(username):
    cursor.execute("DELETE FROM Users WHERE username = ?;", username)

'''
PRECONDITION: no users have been retrieved
POSTCONDITION: formatted records of all users returned
'''
def getAllUsers():
    #for [uID, username, password, user_email, xp] in temp:
        #result = str(uID) + " " + str(username) + " " + str(password) + " " + str(user_email) + " " + str(xp)
    return cursor.execute("SELECT * FROM Users;").fetchall()

# Class Methods
'''
PRECONDITION: no classes have been retrieved from db
POSTCONDITION: all classes for user 'username' have been retrieved (if the class is uncomplete)
'''
def getClasses(username):
    # get user id
    userID = getUser(username).uID
    record = cursor.execute("SELECT * FROM Classes WHERE FK_uID = ? AND is_complete = 0;", userID).fetchall()
    return record


'''
PRECONDITION: class id for individuals unknown
POSTCONDITION: returns classID for specified user and specified class
'''
def getClassID(username, className):
    userID = getUser(username).uID
    record = cursor.execute("SELECT cID FROM Classes WHERE FK_uID = ? AND class_Name =?;", userID, className).fetchone()
    return record.cID
'''
PRECONDITION: no classes retrieved
POSTCONDITION: a single class is returned when given username and class id
'''
def getSingleClass(username, className):
    userID = getUser(username).uID
    classID = getClassID(username, className)
    record = cursor.execute("SELECT * FROM Classes WHERE FK_uID = ? AND cID = ?;", userID, classID).fetchone()
    return record
'''
PRECONDITION: no classes have been added 
POSTCONDITION: specified class for specified user is added to the db and record is returned
'''
def addClass(username, className, timeslot):
    prep_stmt = "INSERT INTO Classes (class_Name, timeslot, FK_uID) VALUES (?,?,?);"
    id = getUser(username).uID
    return cursor.execute(prep_stmt, className, timeslot, id)

'''
PRECONDITION:
POSTCONDITION:
'''
def removeClass(username, className):
    id = getUser(username).uID
    classID = getClassID(username, className)
    record = cursor.execute("DELETE FROM Classes WHERE FK_uID = ? AND cID = ?;", id, classID)
    return record

'''
PRECONDITION: all classes marked uncomplete
POSTCONDITION: specified class marked complete, but not removed from db
'''
def completeClass(username, className):
    classID = getClassID(username, className)
    userID = getUser(username).uID
    prep_stmt = "UPDATE Classes SET is_complete = ? WHERE cID = ? AND FK_uID = ?;"
    record = cursor.execute(prep_stmt, 1, classID, userID)
    return record

'''
PRECONDITION: class data remains unchanged
POSTCONDITION: class data for specified class and user updated using specified information
'''
def editClassMeta(username, className, sectionnum, classroom, prof,
                 prof_email, prof_phone, prof_office, prof_hours):
    userID = getUser(username).uID
    classID = getClassID(username, className)
    # update doesnt return a record
    cursor.execute("UPDATE Classes SET section = ? WHERE FK_uID = ? AND cID = ?",sectionnum, userID, classID)
    cursor.execute("UPDATE Classes SET classroom = ? WHERE FK_uID = ? AND cID = ?", classroom, userID, classID)
    cursor.execute("UPDATE Classes SET prof_Name = ? WHERE FK_uID = ? AND cID = ?", prof, userID, classID)
    cursor.execute("UPDATE Classes SET prof_Email = ? WHERE FK_uID = ? AND cID = ?", prof_email, userID, classID)
    cursor.execute("UPDATE Classes SET prof_Phone = ? WHERE FK_uID = ? AND cID = ?", prof_phone, userID, classID)
    cursor.execute("UPDATE Classes SET prof_Office = ? WHERE FK_uID = ? AND cID = ?", prof_office, userID, classID)
    cursor.execute("UPDATE Classes SET prof_Hours = ? WHERE FK_uID = ? AND cID = ?", prof_hours, userID, classID)
    return

'''
PRECONDITION: the total study time for the class is unchanged
POSTCONDITION: total study time for the specified class for the specified user has been updated with time studied
'''
def addStudyTime(username, className, t):
    userID = getUser(username).uID
    record = getSingleClass(username, className)
    classID = record.cID
    study = record.studyTime
    uTime =  study + t
    prep_stmt = "UPDATE Classes SET studyTime = ? WHERE FK_uID = ? AND cID = ?;"
    return cursor.execute(prep_stmt, uTime, userID, classID)
''''
PRECONDITION: no tasks have been retrieved
POSTCONDITION: list of tasks per class retrieved
'''

# not sprint 2
def getTaskList(username, className):
    userID = getUser(username).uID
    classID = getClassID(className)
    return cursor.execute("SELECT * FROM Tasks WHERE FK_uID = ? AND FK_cID = ?", userID, classID).fetchall()
''''
PRECONDITION: no taskID has been retrieved
POSTCONDITION: taskID for specified user, class and task retrieved
'''
def getTaskID(username, className, taskName):
    userID = getUser(username).uID
    classID = getClassID(className)
    record = cursor.execute("SELECT * FROM Tasks WHERE FK_uID = ? AND FK_cID = ? AND task_Name = ?", userID, classID,
                            taskName)
    return record.tID

''''
PRECONDITION: no tasks have been completed
POSTCONDITION: specifed task has been marked as complete
'''
def completeTask(username, className, taskName, grade):
    taskID = getTaskID(username, className, taskName)
    userID = getUser(username).uID
    classID = getClassID()
    return cursor.execute("UPDATE Tasks SET task_grade = ? WHERE FK_uID = ? AND FK_cID = ? AND tID = ?", grade, userID,
                          classID, taskID)
