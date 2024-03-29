import datetime
import unittest

import flask.app
import flask_unittest
from flask.testing import FlaskClient

import db
import server
import pyodbc
import tempfile


class dbBaseTest(unittest.TestCase):
    '''
       TEST: test_cnxn()
           Test passes if a viable connection to db has been established
           Else, connection failed
       '''

    def test_cnxn(self):
        try:
            # PROD CONNECTION STRING
            conn = (r'Driver=ODBC Driver 17 for SQL Server;'
                    r'Server=localhost;'
                    r'Database=StudyBuddy;'
                    r'UID=sa;'
                    r'PWD=dbtools.IO'
                    )
            # DEV CONNECTION STRING D.N.T
            '''conn = (r'Driver=SQL Server;'
                    r'Server=(local);'
                    r'Database=StudyBuddy;'
                    r'Trusted_Connection=yes'
                    )'''
            cnxn = pyodbc.connect(conn)
        except Exception:
            self.fail("Connection failed")
        cnxn.close()

    ''' 
    TEST: testData()
    Passes if there is data in the users and class tables
    '''

    def testData(self):
        users = db.getUserData()
        self.assertNotEqual(users, None)
        classes = db.getClassesData()
        self.assertNotEqual(classes, None)
        # reset data from load test
        db.editTask("andrea22", "COMP 2080", "Midterm", "Exam", "", "", "")


class dbUserTests(unittest.TestCase):
    '''
        TEST: getUser()
        Test passes if the correct record information is retrieved for the specified username
        Test fails if incorrect record returned
        '''

    def test_getUser(self):
        username = "katDot"
        result = db.getUser(username)
        self.assertIn(username, result.username)

    '''
    TEST: getUserFail()
    Test passes if returns None type for user that doesnt exist in db
    '''

    def test_getUserFail(self):
        username = "test"
        result = db.getUser(username)
        self.assertEqual(result, None)

    '''
    TEST: test_removeUser()
    Test passes if mock user successfully removed from db
    '''

    def test_removeUser(self):
        username = "test"
        password = "testing"
        db.createAccount(username, password)
        # remove user
        db.removeUser(username)
        result = db.getAllUsers()
        self.assertNotIn(username, result)

    '''
    TEST:removeUserFail()
    Test passes if error msg is returned when trying to remove a user that doesnt exist
    '''

    def test_removeUserFail(self):
        username = 'test'
        record = db.removeUser(username)
        self.assertIn("is not in database", record)

    '''
    TEST: test_createAccount()
    Test passes if user is sucessfully inserted into the db (asserting that user appears in retrieved record)
    Mock user is removed at the end of the test
    '''

    def test_createAccount(self):
        username = "test"
        password = "testing"
        result = db.createAccount(username, password)
        self.assertEqual(result, True)
        # retrieve the mock user from the db
        result = db.getUser(username)
        self.assertIn(username, result.username)
        # remove user
        db.removeUser(username)


class dbClassTests(unittest.TestCase):
    '''
        TEST: test_getClasses()
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
    TEST: test_getClassesNone()
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
        self.assertNotIn("test", users)

    '''
    TEST: test_ClassID()
    Test passes if the class ID from the record with username & className matches hardcoded value (3)
    '''

    def test_ClassId(self):
        username = 'katDot'
        className = 'Comp 4350'
        record = db.getClassID(username, className)
        self.assertEqual(3, record)

    '''
    TEST: test_ClassID_AttrError()
    Test passes if None guard present in function <getClassID> is working; ie no attribute errors thrown
    '''

    def test_ClassId_AttrError(self):
        username = 'katDot'
        className = 'fake class'
        record = db.getClassID(username, className)
        self.assertEqual(record, None)

    '''
    TEST: test_getSingleClass()
    Test passes if the hardcoded username and className appear in the requested record
    '''

    def test_getSingleClass(self):
        username = 'katDot'
        className = "COMP 4350"
        record = db.getSingleClass(username, className)
        self.assertIn(className, record)

    '''
    TEST: test_addClass()
    Test passes if the added class can be successfully retrieved from the db
    '''

    def test_addClass(self):
        username = 'katDot'
        className = "COMP 2080"
        timeslot = "16:00:00.0000000"
        db.addClass(username, className, timeslot, None)
        result = db.getSingleClass(username, className)
        self.assertIn(className, result)
        # remove class once done
        db.removeClass(username, className)

    '''
    TEST test_addClassCode()
    Test passes if a classCode was sucessfully added to the specified class for the specfied user.
    '''

    def test_addClassCode(self):
        username = 'katDot'
        className = "COMP 2080"
        timeslot = "16:00:00.0000000"
        code = "12345"
        db.addClass(username, className, timeslot, code)
        result = db.getSingleClass(username, className)
        self.assertIn(className, result)
        self.assertIn(code, result)
        # remove class once done
        db.removeClass(username, className)

    '''
    TEST: test_removeClass()
    Test passes if the added class is successfully removed from the db (no longer appears in class list)
    '''

    def test_removeClass(self):
        username = 'katDot'
        className = "COMP 2080"
        timeslot = "9:00:00.0000000"
        db.addClass(username, className, timeslot, None)
        # remove it
        db.removeClass(username, className)
        record = db.getClasses(username)
        for i in range(len(record)):
            self.assertNotIn(className, record[i])

    '''
    TEST: test_completeClass()
    Test passes if is_complete value for specified class is 1
    '''

    def test_completeClass(self):
        username = 'katDot'
        className = "COMP 2150"
        timeslot = "9:00:00.0000000"
        # add new class to complete
        db.addClass(username, className, timeslot, None)
        db.completeClass(username, className)
        record = db.getSingleClass(username, "COMP 2150")
        self.assertEqual(1, record.is_complete)
        # remove
        db.removeClass(username, className)

    '''
    TEST: test_addStudyTime_base()
    Test passes if new study time matches hardcoded value
    '''

    def test_addStudyTime_base(self):
        username = "katDot"
        className = "COMP 2150"
        timeslot = "9:00:00.0000000"
        db.addClass(username, className, timeslot, None)
        db.addStudyTime(username, className, 1.30)
        record = db.getSingleClass(username, className)
        self.assertEqual(record.studyTime, 1.30)

    '''
    TEST: test_editClassMeta
    Test passes if each column in specified class was successfully updated with new metadata
    NOTE: can fail in the local backend suite, but will pass in the github test suite
    --> has to do with asserting the datetime obj locally (environment issues)
    '''

    def test_editClassMeta(self):
        username = "katDot"
        className = "COMP 2150"
        timeslot = "9:00:00.0000000"
        db.addClass(username, className, timeslot, None)
        db.editClassMeta(username, className, "", "", "", "", "",
                         "", "")
        db.editClassMeta(username, className, "A01", "320 Machray", "Steve Stevenson", "Steve@steve.com", "999-9999",
                         "150 EITC", "10:00:00")
        record = db.getSingleClass(username, className)
        u = db.getUser(username).uID
        c = db.getClassID(username, className)
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

    '''
    TEST: test_addClassBreakdown()
     Test passes if the given breakdown matches the breakdown returned in the record
    '''

    def test_addClassBreakdown(self):
        username = 'katDot'
        className = 'COMP 3820'
        breakdown = '{"A+":"(95,100)", "A":"(80,94)", "B+":"(75,79)", "B":"(70,74)", "C+":"(65,69)", "C":"(56,64)", "D":"(50,55)", "F":"(0, 49)"}'
        db.addClassBreakdown(username, className, breakdown)
        record = db.getSingleClass(username, className)
        self.assertNotEqual(record, None)
        self.assertEqual(breakdown, record.breakdown)

    '''
    TEST: test_editClassReqData_Name()
    Test passes if required class field 'className' is correctly updated to new className, for given user
    '''

    def test_editClassReqData_Name(self):
        username = "katDot"
        className_old = "COMP 3820"
        className_new = "Bioinformatics"
        orig = db.getSingleClass(username, className_old)
        self.assertNotEqual(orig, None)
        db.editClassReqData(username, className_old, className_new, "")
        record = db.getSingleClass(username, className_new)
        self.assertNotEqual(record, orig)
        # reset
        db.editClassReqData(username, className_new, className_old, "")
        record = db.getSingleClass(username, className_old)
        self.assertEqual(record, orig)

    '''
    TEST: test_editClassReqData_Timeslot()
    Test passes if required class field 'timeslot' is correctly updated to new timeslot, for given user and class
    '''

    def test_editClassReqData_Timeslot(self):
        username = "katDot"
        className = "COMP 3820"
        timeslot_old = "14:30:00"
        timeslot_new = "10:00:00"
        orig = db.getSingleClass(username, className)
        self.assertNotEqual(orig, None)
        db.editClassReqData(username, className, "", timeslot_new)
        record = db.getSingleClass(username, className)
        self.assertNotEqual(record, orig)
        # reset
        db.editClassReqData(username, className, "", timeslot_old)
        record = db.getSingleClass(username, className)
        self.assertEqual(record, orig)


class dbTaskTests(unittest.TestCase):
    '''
      TEST: test_getTaskList()
      Test passes if task list for specified user returned successfully
      '''

    def test_getTaskList(self):
        username = "katDot"
        className = "COMP 3820"
        record = db.getTaskList(username, className)
        self.assertNotEqual(record, None)

    '''
    TEST: test_getEmptyTasks()
    Test passes if username, className has no tasks
    '''

    def test_getEmptyTasks(self):
        username = "ryan2023"
        className = "COMP 4350"
        record = db.getTaskList(username, className)
        self.assertEqual(record, None)

    '''
    TEST: test_getTaskID()
    Test passes if correct taskID returned when given specified username and class
    '''

    def test_getTaskID(self):
        username = "katDot"
        className = "COMP 3820"
        taskName = "A1"
        record = db.getTaskID(username, className, taskName)
        self.assertEqual(record.tID, 1)

    '''
    TEST: test_getTaskIDFail()
    Test passes if None guard in <getTaskID> is working
    '''

    def test_getTaskIDFail(self):
        username = "katDot"
        className = "COMP 3820"
        taskName = "A2"
        record = db.getTaskID(username, className, taskName)
        self.assertEqual(record, None)

    '''
    TEST: test_completeTask()
    Test passes if Task with the grade (ie newly completed task) appears in the list of completed tasks
    '''

    def test_completeTask(self):
        username = "katDot"
        className = "COMP 3820"
        taskName = "A1"
        db.completeTask(username, className, taskName, 98)
        record = db.getCompleteTasksForClass(username, className)
        self.assertNotEqual(record, None)
        self.assertEqual(record[0].task_grade, 98)

    '''
    TEST: test_uncompleteTask()
    Test passes if completed task is successfully reset to be uncompleted (ie not in completed tasks and grade = 0.0)
    '''

    def test_uncompleteTask(self):
        username = "katDot"
        className = "COMP 3820"
        taskName = "A1"
        db.uncompleteTask(username, className, taskName)
        record = db.getCompleteTasksForClass(username, className)
        self.assertEqual(record, None)
        record = db.getTaskList(username, className)
        self.assertEqual(record[0].task_grade, 0)

    '''
    TEST: test_getCompleteTasksForClassSingle()
    Test passes if the single, completed task appears in the list
    '''

    def test_getCompleteTasksForClassSingle(self):
        username = "andrea22"
        className = "COMP 2080"
        taskID = db.getTaskID(username, className, "A1").tID
        record = db.getCompleteTasksForClass(username, className)
        self.assertEqual(record[0].tID, taskID)

    '''
    TEST: test_getCompleteTasksForClassMulti
    Test passes if all complete tasks appear in the list
    '''

    def test_getCompleteTasksForClassMulti(self):
        username = "andrea22"
        className = "COMP 2080"
        task1ID = db.getTaskID(username, className, "A1")
        task2ID = db.getTaskID(username, className, "Exam")
        db.completeTask(username, className, "Exam", 88)
        record = db.getCompleteTasksForClass(username, className)
        self.assertNotEqual(record, None)
        task1 = ["A1", task1ID]
        task2 = ["Exam", task2ID]
        self.assertEqual(any(x in task2 for x in record[0]), True)
        self.assertEqual(any(x in task1 for x in record[1]), True)
        # mark "Exam" as uncomplete
        db.uncompleteTask(username, className, "Exam")

    '''
    TEST: test_getSingleTask()
    Test passes if the requested task [name, id] appears in result of single task request
    '''

    def test_getSingleTask(self):
        username = "katDot"
        className = "COMP 3820"
        record = db.getSingleTask(username, className, "A1")
        self.assertNotEqual(record, None)
        task = ["A1", 1]
        self.assertEqual(any(x in task for x in record), True)

    '''
    TEST: test_removeTask()
    Test passes if specified task is correctly removed from the db
    '''

    def test_removeTask(self):
        username = "katDot"
        className = "COMP 3820"
        record = db.addTask(username, className, "Final Exam", 50, "2023-04-20 23:59:00", None)
        self.assertNotEqual(record, None)
        db.removeTask(username, className, "Final Exam")
        task = db.getSingleTask(username, className, "Final Exam")
        self.assertEqual(task, None)

    '''
    TEST: test_addTask()
    Test passes if task specified appears in the db for the specified user and class
    '''

    def test_addTask(self):
        username = "katDot"
        className = "COMP 3820"
        record = db.addTask(username, className, "Final Exam", 50, "2023-04-20 23:59:00", None)
        self.assertNotEqual(record, None)
        task = db.getSingleTask(username, className, "Final Exam")
        self.assertIn("Final Exam", task)
        db.removeTask(username, className, "Final Exam")

    '''
    TEST: test_editTask()
    Test passes if task was successfully edited
    '''

    def test_editTask(self):
        username = "katDot"
        className = "COMP 3820"
        record = db.getSingleTask(username, className, "A1")
        self.assertNotEqual(record, None)
        db.editTask(username, className, "A1", "", "2023-04-20 23:59:00", 0, "B")
        # get edited record
        nRecord = db.getSingleTask(username, className, "A1")
        self.assertNotEqual(record, nRecord)
        d1 = datetime.datetime(year=2023, month=2, day=9, hour=14, minute=0, second=0)
        d2 = datetime.datetime(year=2023, month=4, day=20, hour=23, minute=59, second=0)
        self.assertEqual(nRecord.deadline, d2)
        # return record to default state
        db.editTask(username, className, "A1", '', '2023-02-09 14:00:00', 0, "A")
        record = db.getSingleTask(username, className, "A1")
        self.assertEqual(record.deadline, d1)

    '''
    TEST: test_getDeadlines()
    Test passes if retrieved deadlines match the given deadlines
    '''

    def test_getDeadlines(self):
        username = 'katDot'
        d1 = datetime.datetime(year=2023, month=2, day=9, hour=14, minute=0, second=0)
        record = db.getDeadlines(username)
        self.assertNotEqual(record, None)
        self.assertEqual(record[0].deadline, d1)


creds = {'username': 'ryan2023', 'password': '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'}
creds2 = {'username': 'newuser', 'password': 'd74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1'}
# ^ password = pass
creds3 = {'username': 'andrea22', 'password': 'edee29f882543b956620b26d0ee0e7e950399b1c4222f5de05e06425b4c995e9'}


class apiUsersTest(flask_unittest.ClientTestCase):
    # assign flask app
    app = server.app

    def setUp(self, client: FlaskClient):
        pass

    def tearDown(self, client: FlaskClient):
        client.delete_cookie('127.0.0.1:5000', 'session')

    def test_login(self, client: FlaskClient):
        # send post request to login api
        resp = client.post("/api/login", json=creds)
        # check the status
        self.assertStatus(resp, 200)
        resp = client.post("/api/login", json=creds3)
        self.assertStatus(resp, 200)

    def test_login_nouser(self, client: FlaskClient):
        # send post request to login api
        resp = client.post("/api/login", json={'username': 'notauser', 'password': 'password'})
        # check the status
        self.assertStatus(resp, 401)

    def test_login_wrongpass(self, client: FlaskClient):
        # send post request to login api
        resp = client.post("/api/login", json={'username': 'ryan2023', 'password': 'notthepassword'})
        # check the status
        self.assertStatus(resp, 401)

    def test_logout_fail(self, client):
        resp = client.post('/api/logout')
        self.assertStatus(resp, 401)

    def test_logout(self, client):
        # log in
        resp = client.post('/api/login', json=creds)
        # check valid login
        self.assertStatus(resp, 200)

        session = resp.headers['session']
        # send post request to log out
        resp = client.post('/api/logout', headers={"session": session})
        # expect session no longer set
        self.assertStatus(resp, 200)

    def test_newUser(self, client):
        db.removeUser("newuser")
        # send invalid login to ensure user doesn't exist
        resp = client.post('/api/login', json=creds2)
        self.assertStatus(resp, 401)
        # create user
        resp = client.post('/api/newuser', json=creds2)
        self.assertStatus(resp, 200)
        # log in as user
        resp = client.post('/api/login', json=creds2)
        self.assertStatus(resp, 200)
        # remove user after test is done
        db.removeUser("newuser")


class apiClassTests(flask_unittest.ClientTestCase):
    # assign flask app
    app = server.app

    def setUp(self, client: FlaskClient):
        pass

    def tearDown(self, client: FlaskClient):
        client.delete_cookie('127.0.0.1:5000', 'session')

    def test_allclasses(self, client):
        # log in
        resp = client.post('/api/login', json=creds)
        # check valid login
        self.assertStatus(resp, 200)
        # send request for all classes
        resp = client.get('/api/class')
        # check valid status
        self.assertStatus(resp, 200)

    def test_class(self, client):
        # log in
        resp = client.post('/api/login', json=creds)
        # check valid login
        self.assertStatus(resp, 200)
        # send request for one class
        resp = client.get('/api/class/COMP 4350')
        self.assertStatus(resp, 200)

    def test_class_fail(self, client):
        # log in
        resp = client.post('/api/login', json=creds)
        # check valid login
        self.assertStatus(resp, 200)
        # send request for one class
        resp = client.get('/api/class/notaclass')
        self.assertStatus(resp, 400)

    def test_update_time(self, client):
        # log in
        resp = client.post('/api/login', json=creds)
        # check valid login
        self.assertStatus(resp, 200)
        # send update request
        resp = client.post('/api/class/COMP 4350/update_time', json={'added': 1024})
        # check success
        self.assertStatus(resp, 200)

    def test_update_time_fail(self, client):
        # log in
        resp = client.post('/api/login', json=creds)
        # check valid login
        self.assertStatus(resp, 200)
        # send update request
        resp = client.post('/api/class/NOTACLASS/update_time', json={'added': 1024})
        # check fail
        self.assertStatus(resp, 400)

    def test_newclass(self, client):
        # log in
        resp = client.post('/api/login', json=creds)
        # check valid login
        self.assertStatus(resp, 200)
        # create new class
        resp = client.post('/api/newclass',
                           json={"classname": "COMP 9999", "timeslot": "11:30:00", "courseCode": ""})
        self.assertStatus(resp, 200)
        # double check class exists
        resp = client.get('/api/class/COMP 9999')
        self.assertStatus(resp, 200)
        resp = client.get('/api/class')
        #remove class
        resp = client.post('/api/class/COMP 9999/delete')
        self.assertStatus(resp,200)

    def test_updatemeta(self, client):
        # log in
        resp = client.post('/api/login', json={'username': 'katDot',
                                               'password': '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4'})
        # check valid login
        self.assertStatus(resp, 200)
        # update metadata
        resp = client.post('/api/class/COMP 3820/update_meta', json={
            "breakdown": '{"A+":"(90,100)", "A":"(80,89)", "B+":"(75,79)", "B":"(70,74)", "C+":"(65,69)", "C":"(56,64)", "D":"(50,55)", "F":"(0, 49)"}',
            "prof_email": "email@prof.com"})

        self.assertStatus(resp, 200)
        # ensure update
        resp = client.get('/api/class/COMP 3820')
        self.assertEqual(resp.get_json(force=True)["result"]["prof_Email"], "email@prof.com")

    def test_editclass(self, client):
        # log in
        resp = client.post('/api/login', json=creds)
        # check valid login
        self.assertStatus(resp, 200)
        # create class
        resp = client.post('/api/newclass',
                           json={"classname": "COMP 123", "timeslot": "11:30:00", "courseCode": None})
        self.assertStatus(resp, 200)
        # edit class
        resp = client.get('/api/class/COMP 123')
        resp = client.post('/api/class/COMP 123/edit', json={"newname": "COMP 8888"})
        self.assertStatus(resp, 200)
        resp = client.get('/api/class')
        # double check
        resp = client.get('/api/class/COMP 8888')
        # name changed
        self.assertStatus(resp, 200)
        # timeslot didn't change
        self.assertEqual(resp.get_json(force=True)['result']['timeslot'], "11:30:00")
        # remove class
        resp = client.post('/api/class/COMP 8888/delete')
        self.assertStatus(resp, 200)

    def test_completeclass(self, client):
        # log in
        resp = client.post('/api/login', json={"username": "sneakerbot101",
                                               "password": '73b2e90162bdd5ff6151294bee6fa72d602680e29b0bcb6702f952262ffb7055'})
        # check valid login
        self.assertStatus(resp, 200)
        # complete class
        resp = client.post('/api/class/COMP 4350/complete')
        self.assertStatus(resp, 200)

    def test_deleteclass(self, client):
        # log in
        resp = client.post('/api/login', json={"username": "EliStudy",
                                               "password": '3459d4e034fb958e5f6c836ac00558ee7a614c0234a55f4df16535845a6cb186'})
        # check valid login
        self.assertStatus(resp, 200)
        # delete class
        resp = client.post('/api/class/COMP 4350/delete')
        self.assertStatus(resp, 200)
        # ensure class is gone
        resp = client.get('/api/class/COMP 4350')
        self.assertStatus(resp, 400)
        #now put it back
        resp = client.post('/api/newclass', json={"classname": "COMP 4350", "timeslot": "11:30:00", "courseCode": ""})
        self.assertStatus(resp,200)

class apiTaskTests(flask_unittest.ClientTestCase):
    # assign flask app
    app = server.app

    def setUp(self, client: FlaskClient):
        pass

    def tearDown(self, client: FlaskClient):
        client.delete_cookie('127.0.0.1:5000', 'session')

    def test_task(self, client):
        # log in
        resp = client.post('/api/login', json={'username': 'andrea22',
                                               'password': 'edee29f882543b956620b26d0ee0e7e950399b1c4222f5de05e06425b4c995e9'})
        # check valid login
        self.assertStatus(resp, 200)
        resp = client.get('/api/class/COMP 2080/task/Exam')
        self.assertStatus(resp, 200)

    def test_task_fail1(self, client):
        # log in
        resp = client.post('/api/login', json=creds)
        # check valid login
        self.assertStatus(resp, 200)
        resp = client.get('/api/class/NotACLass/task/NotATask')
        self.assertStatus(resp, 400)

    def test_task_fail2(self, client):
        # log in
        resp = client.post('/api/login', json=creds)
        # check valid login
        self.assertStatus(resp, 200)
        resp = client.get('/api/class/COMP 4350/task/NotATask')
        self.assertStatus(resp, 400)

    def test_alltasks(self, client):
        # log in
        resp = client.post('/api/login', json={'username': 'andrea22',
                                               'password': 'edee29f882543b956620b26d0ee0e7e950399b1c4222f5de05e06425b4c995e9'})
        # check valid login
        self.assertStatus(resp, 200)
        resp = client.get('/api/class/COMP 2080/task')
        self.assertStatus(resp, 200)

    def test_newtask(self, client):
        # log in
        resp = client.post('/api/login', json={'username': 'andrea22',
                                               'password': 'edee29f882543b956620b26d0ee0e7e950399b1c4222f5de05e06425b4c995e9'})
        # check valid login
        self.assertStatus(resp, 200)
        resp = client.post('/api/class/COMP 4350/newtask', json={'taskname': 'Study some stuff'})
        self.assertStatus(resp, 200)
        #remove task
        resp = client.post('/api/class/COMP 4350/task/Study some stuff/delete')
        self.assertStatus(resp,200)

    def test_complete_task(self, client):
        # log in
        resp = client.post('/api/login', json={'username': 'andrea22',
                                               'password': 'edee29f882543b956620b26d0ee0e7e950399b1c4222f5de05e06425b4c995e9'})
        # check valid login
        self.assertStatus(resp, 200)
        resp = client.get('/api/class/COMP 2080/task')
        resp = client.post('/api/class/COMP 2080/task/Exam/complete', json={"grade": "97"})
        self.assertStatus(resp, 200)
        resp = client.get('/api/class/COMP 2080/task')

    def test_complete_task_fail(self, client):
        # log in
        resp = client.post('/api/login', json={'username': 'andrea22',
                                               'password': 'edee29f882543b956620b26d0ee0e7e950399b1c4222f5de05e06425b4c995e9'})
        # check valid login
        self.assertStatus(resp, 200)
        resp = client.post('/api/class/COMP 2080/task/task1/complete')
        self.assertStatus(resp, 400)

    def test_grade(self, client):
        # log in
        resp = client.post('/api/login', json={'username': 'andrea22',
                                               'password': 'edee29f882543b956620b26d0ee0e7e950399b1c4222f5de05e06425b4c995e9'})
        # check valid login
        self.assertStatus(resp, 200)
        # get grade for class
        resp = client.get('/api/class/COMP 2080/grade')
        self.assertStatus(resp, 200)

    def test_grade_notasks(self, client):
        # log in
        resp = client.post('/api/login', json={'username': 'andrea22',
                                               'password': 'edee29f882543b956620b26d0ee0e7e950399b1c4222f5de05e06425b4c995e9'})
        # check valid login
        self.assertStatus(resp, 200)
        # get grade for class
        resp = client.get('/api/class/COMP 4350/grade')
        self.assertStatus(resp, 200)

    def test_edittask(self, client):
        # log in
        resp = client.post('/api/login', json=creds)
        # check valid login
        self.assertStatus(resp, 200)
        # new task
        resp = client.post('/api/class/COMP 4350/newtask',
                           json={'taskname': 'Not Final', "weight": 10, "deadline": "2023-02-16 10:00:00"})
        self.assertStatus(resp, 200)
        # edit task
        resp = client.post('/api/class/COMP 4350/task/Not Final/edit',
                           json={"newname": "Final Exam", "newweight": 40})
        self.assertStatus(resp, 200)
        # ensure only desired changes were made
        resp = client.get('/api/class/COMP 4350/task/Final Exam')
        # ensure name change
        self.assertStatus(resp, 200)
        # deadline didn't change
        self.assertEqual(resp.get_json(force=True)['result']['deadline'], '2023-02-16 10:00:00')
        # weight did change
        self.assertEqual(resp.get_json(force=True)['result']['task_Weight'], 40)
        resp = client.post('/api/class/COMP 4350/task/Final Exam/delete')

    def test_deletetask(self, client):
        # log in
        resp = client.post('/api/login', json=creds)
        # check valid login
        self.assertStatus(resp, 200)
        # new task
        resp = client.post('/api/class/COMP 4350/newtask',
                           json={'taskname': 'Final', 'weight': 70, 'deadline': '2023-02-16 10:00', 'task_goal': None})
        self.assertStatus(resp, 200)
        # delete task
        resp = client.post('/api/class/COMP 4350/task/Final/delete')
        self.assertStatus(resp, 200)
        # ensure task is gone
        resp = client.get('/api/class/COMP 4350/task/Final')
        self.assertStatus(resp, 400)

    def test_donetasks(self, client):
        # log in
        resp = client.post('/api/login', json={'username': 'andrea22',
                                               'password': 'edee29f882543b956620b26d0ee0e7e950399b1c4222f5de05e06425b4c995e9'})
        # check valid login
        self.assertStatus(resp, 200)
        # grab graded tasks
        resp = client.get('/api/class/COMP 2080/done_tasks')
        self.assertStatus(resp, 200)


if __name__ == '__main__':
    unittest.main()
