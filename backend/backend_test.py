import datetime
import unittest

import flask.app
import flask_unittest
from flask.testing import FlaskClient

import db
import server
import pyodbc
import tempfile


class dbTests(unittest.TestCase):
    '''
        Test passes if a viable connection to db has been established
        Else, connection failed
    '''

    def test_cnxn(self):
        try:
            # PROD CONNECTION STRING
            '''conn = (r'Driver=ODBC Driver 17 for SQL Server;'
                    r'Server=localhost;'
                    r'Database=StudyBuddy;'
                    r'UID=sa;'
                    r'PWD=dbtools.IO'
                    )'''
            # DEV CONNECTION STRING D.N.T
            conn = (r'Driver=SQL Server;'
                    r'Server=(local);'
                    r'Database=StudyBuddy;'
                    r'Trusted_Connection=yes'
                    )
            cnxn = pyodbc.connect(conn)
        except Exception:
            self.fail("Connection failed")
        cnxn.close()

    '''
    Test passes if the correct record information is retrieved for the specified username
    Test fails if incorrect record returned
    '''
    def test_getUser(self):
        username = "katDot"
        result = db.getUser(username)
        self.assertIn(username, result.username)
    '''
    Test passes if returns None type for user that doesnt exist in db
    '''
    def test_getUserFail(self):
        username = "test"
        result = db.getUser(username)
        self.assertEqual(result, None)

    '''
    Test passes if mock user successfully removed from db
    '''
    def test_removeUser(self):
        username = "test"
        # db.removeUser(username)
        password = "testing"
        db.createAccount(username, password)
        # remove user
        db.removeUser(username)
        result = db.getAllUsers()
        self.assertNotIn(username, result)

    '''
    Test passes if error msg is returned when trying to remove a user that doesnt exist
    '''
    def test_removeUserFail(self):
        username = 'test'
        record = db.removeUser(username)
        self.assertIn("is not in database", record)

    '''
    Test passes if user is sucessfully inserted into the db (asserting that user appears in retrieved record)
    Mock user is removed at the end of the test
    '''

    def test_createAccount(self):
        username = "test"
        password = "testing"
        db.createAccount(username, password)
        # retrieve the mock user from the db
        result = db.getUser(username)
        self.assertIn(username, result.username)
        # remove user
        db.removeUser(username)

    # Class Tests
    '''
    Test passes if given strings are present in the record retrieved
    '''
    def test_getClasses(self):
        username = "katDot"
        c1 = "COMP 4350"
        c2 = "COMP 3820"
        classes = db.getClasses(username)
        self.assertIn(c1, classes[0])
        self.assertIn(c2, classes[1])
    '''
    Test passes if the None guards present in the function <getClasses> is working
    '''
    def test_getClassesNone(self):
        username = "test"
        password = "1234"
        db.createAccount(username, password)
        classes = db.getClasses(username)
        self.assertEqual(classes, None)
        db.removeUser(username)
        users = db.getAllUsers()
        self.assertNotIn("test",users)
    '''
    Test passes if the class ID from the record with username & className matches hardcoded value (3)
    '''
    def test_ClassId(self):
        username = 'katDot'
        className = 'Comp 4350'
        record = db.getClassID(username, className)
        self.assertEqual(3, record)

    '''
    Test passes if None guard present in function <getClassID> is working; ie no attribute errors thrown
    '''
    def test_ClassId_AttrError(self):
        username = 'katDot'
        className = 'fake class'
        record = db.getClassID(username, className)
        self.assertEqual(record,None)

    '''
    Test passes if the hardcoded username and className appear in the requested record
    '''

    def test_getSingleClass(self):
        username = 'katDot'
        className = "COMP 4350"
        record = db.getSingleClass(username, className)
        self.assertIn(className, record)

    '''
    Test passes if the added class can be successfully retrieved from the db
    '''

    def test_addClass(self):
        username = 'katDot'
        className = "COMP 2080"
        timeslot = "16:00:00.0000000"
        db.addClass(username, className, timeslot)
        result = db.getSingleClass(username, className)
        self.assertIn(className, result)
        # remove class once done
        db.removeClass(username, className)

    '''
    Test passes if the added class is successfully removed from the db (no longer appears in class list)
    '''

    def test_removeClass(self):
        username = 'katDot'
        className = "COMP 2150"
        timeslot = "9:00:00.0000000"
        db.addClass(username, className, timeslot)
        # remove it
        db.removeClass(username, className)
        record = db.getClasses(username)
        for i in range(len(record)):
            self.assertNotIn(className, record[i])

    '''
    Test passes if is_complete value for specified class is 1
    '''

    def test_completeClass(self):
        username = 'katDot'
        className = "COMP 2150"
        timeslot = "9:00:00.0000000"
        # add new class to complete
        db.addClass(username, className, timeslot)
        db.completeClass(username, className)
        record = db.getSingleClass(username, "COMP 2150")
        self.assertEqual(1, record.is_complete)
        # remove
        db.removeClass(username, className)

    '''
    Test passes if new study time matches hardcoded value
    '''

    def test_addStudyTime_base(self):
        username = "katDot"
        className = "COMP 2150"
        timeslot = "9:00:00.0000000"
        db.addClass(username, className, timeslot)
        db.addStudyTime(username, className, 1.30)
        record = db.getSingleClass(username, className)
        self.assertEqual(record.studyTime, 1.30)

    '''
    Test passes if each column in specified class was successfully updated with new metadata
    NOTE: this fails in the local backend suite, but passes in the github test suite
    --> has to do with asserting the datetime obj locally
    '''
    def test_editClassMeta(self):
        username = "katDot"
        className = "COMP 2150"
        timeslot = "9:00:00.0000000"
        db.addClass(username, className, timeslot)
        db.editClassMeta(username, className, "", "", "", "", "",
                         "", "")
        db.editClassMeta(username, className, "A01", "320 Machray", "Steve Stevenson", "Steve@steve.com", "999-9999",
                         "150 EITC", "10:00:00")
        record = db.getSingleClass(username, className)
        print(record)
        u = db.getUser(username).uID
        print(u)
        c = db.getClassID(username, className)
        print(c)
        self.assertNotEqual(record, None)
        self.assertNotEqual(u, None)
        self.assertNotEqual(c, None)
        self.assertEqual("A01", record.section)
        self.assertEqual("320 Machray", record.classroom)
        self.assertEqual("Steve Stevenson", record.prof_Name)
        self.assertEqual("Steve@steve.com", record.prof_Email)
        self.assertEqual("999-9999", record.prof_Phone)
        self.assertEqual("150 EITC", record.prof_Office)
        d = datetime.datetime.strptime("10:00:00", '%H:%M:%S').time()
        self.assertEqual(d, record.prof_Hours)
# Tasks tests
    '''
    Test passes if task list for specified user returned successfully
    '''
    def test_getTaskList(self):
        username = "katDot"
        className = "COMP 3820"
        record = db.getTaskList(username, className)
        self.assertNotEqual(record, None)
    '''
    Test passes if username, className has no tasks
    '''
    def test_getEmptyTasks(self):
        username = "ryan2023"
        className = "COMP 4350"
        record = db.getTaskList(username,className)
        self.assertEqual(record, None)

    '''
    Test passes if correct taskID returned when given specified username and class
    '''
    def test_getTaskID(self):
        username = "katDot"
        className = "COMP 3820"
        taskName = "A1"
        record = db.getTaskID(username, className, taskName)
        self.assertEqual(record.tID,1)
    '''
    Test passes if None guard in <getTaskID> is working
    '''
    def test_getTaskIDFail(self):
        username = "katDot"
        className = "COMP 3820"
        taskName = "A2"
        record = db.getTaskID(username, className, taskName)
        self.assertEqual(record, None)
    '''
    Test passes if Task with the grade (ie newly completed task) appears in the list of completed tasks
    '''
    def test_completeTask(self):
        username = "katDot"
        className = "COMP 3820"
        taskName = "A1"
        db.completeTask(username,className, taskName, 0.98)
        record = db.getCompleteTasksForClass(username, className)
        self.assertNotEqual(record, None)
        self.assertEqual(record[0].task_grade, 0.98)

    '''
    Test passes if completed task is successfully reset to be uncompleted (ie not in completed tasks and grade = 0.0)
    '''
    def test_uncompleteTask(self):
        username = "katDot"
        className = "COMP 3820"
        taskName = "A1"
        db.uncompleteTask(username,className,taskName)
        record = db.getCompleteTasksForClass(username, className)
        self.assertEqual(record, None)
        record = db.getTaskList(username, className)
        self.assertEqual(record[0].task_grade, 0.0)
    '''
    Test passes if a all completed tasks appear in the list
    '''
    def test_getCompleteTasksForClassSingle(self):
        username = "andrea22"
        className = "COMP 2080"
        taskID = db.getTaskID(username, className,"A1").tID
        record = db.getCompleteTasksForClass(username,className)
        self.assertEqual(record[0].tID,taskID)
    def test_getCompleteTasksForClassMulti(self):
        username = "andrea22"
        className = "COMP 2080"
        task1ID = db.getTaskID(username,className,"A1")
        task2ID = db.getTaskID(username,className,"Exam")
        db.completeTask(username,className,"Exam",.88)
        record = db.getCompleteTasksForClass(username, className)
        self.assertNotEqual(record, None)
        task1 = ["A1", task1ID]
        task2 = ["Exam", task2ID]
        self.assertEqual(any(x in task2 for x in record[0]), True)
        self.assertEqual(any(x in task1 for x in record[1]), True)
        #mark "Exam" as uncomplete
        db.uncompleteTask(username,className,"Exam")

    #//TODO: add guard tests for complete, uncomplete, complete tasks per class
class apiTest(flask_unittest.ClientTestCase):
    # assign flask app
    app = server.app

    # server.setTest(True)

    def setUp(self, client: FlaskClient):
        pass

    def tearDown(self, client: FlaskClient):
        pass

    def test_login(self, client: FlaskClient):
        # send post request to login api
        resp = client.post("/api/login", json={'username': 'ryan2023', 'password': 'password'})
        # check the status
        self.assertStatus(resp, 200)

    def test_logout(self, client):
        # log in
        resp = client.post('/api/login', json={'username': 'ryan2023', 'password': 'password'})
        # check valid login
        self.assertStatus(resp, 200)
        # send post request to log out
        resp = client.post('/api/logout')
        # expect session no longer set
        self.assertStatus(resp, 200)

    def test_newuser(self, client):
        # send invalid login to ensure user doesn't exist
        resp = client.post('/api/login', json={'username': 'newuser', 'password': 'pass'})
        self.assertStatus(resp, 400)
        # create user
        resp = client.post('/api/newuser', json={'username': 'newuser', 'password': 'pass'})
        self.assertStatus(resp, 200)
        # log in as user
        resp = client.post('/api/login', json={'username': 'newuser', 'password': 'pass'})
        self.assertStatus(resp, 200)

    def test_allclasses(self, client):
        # log in
        resp = client.post('/api/login', json={'username': 'ryan2023', 'password': 'password'})
        # check valid login
        self.assertStatus(resp, 200)
        # send request for all classes
        resp = client.get('/api/class')
        # check valid status
        self.assertStatus(resp, 200)

    def test_class(self, client):
        # log in
        resp = client.post('/api/login', json={'username': 'ryan2023', 'password': 'password'})
        # check valid login
        self.assertStatus(resp, 200)
        # send request for one class
        resp = client.get('/api/class/COMP 4350')
        print(resp.get_data())
        self.assertStatus(resp, 200)

    def test_update_time(self, client):
        # log in
        resp = client.post('/api/login', json={'username': 'ryan2023', 'password': 'password'})
        # check valid login
        self.assertStatus(resp, 200)
        # send update request
        resp = client.post('/api/class/COMP 4350/update_time', json={'added': 1024})
        # check success
        self.assertStatus(resp, 200)


if __name__ == '__main__':
    unittest.main()
