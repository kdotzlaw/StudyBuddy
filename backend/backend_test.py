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
    Test passes if the correct record information is retrieved for the specified username
    Test fails if incorrect record returned, or
    '''

    def test_getUser(self):
        username = 'katDot'
        result = db.getUser(username)

        self.assertIn(username, result.username)

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
    Test passes if the class ID from the record with username & className matches hardcoded value (3)
    '''

    def test_ClassId(self):
        username = 'katDot'
        className = 'Comp 4350'
        record = db.getClassID(username, className)
        self.assertEqual(3, record)

    def test_getSingleClass(self):
        username = 'katDot'
        className = "COMP 4350"
        record = db.getSingleClass(username, className)
        self.assertIn(className, record)

    def test_addClass(self):
        username = 'katDot'
        className = "COMP 2080"
        timeslot = "16:00:00.0000000"
        db.addClass(username, className, timeslot)
        result = db.getSingleClass(username, className)
        self.assertIn(className, result)
        # remove class once done
        db.removeClass(username, className)

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

    def test_completeClass(self):
        username = 'katDot'
        className = "COMP 2150"
        timeslot = "9:00:00.0000000"
        # add new class to complete
        db.addClass(username, className, timeslot)
        db.completeClass(username, className)
        record = db.getSingleClass(username, "COMP 2150")
        print(record)
        self.assertEqual(1, record.is_complete)
        # remove
        db.removeClass(username, className)

    def test_addStudyTime_base(self):
        username = "katDot"
        className = "COMP 2150"
        timeslot = "9:00:00.0000000"
        db.addClass(username, className, timeslot)
        db.addStudyTime(username, className, 1.30)
        record = db.getSingleClass(username, className)
        self.assertEqual(record.studyTime, 1.30)
        #reset studytime
        db.addStudyTime(username, className, -1.30)
        record = db.getSingleClass(username, className)
        self.assertEqual(record.studyTime, 0.0)


    #def test_addStudyTime_existing(self):
    
    def test_editClassMeta(self):
        username = "katDot"
        className = "COMP 2150"
        timeslot = "9:00:00.0000000"
        db.addClass(username, className, timeslot)
        db.editClassMeta(username, className, "A01", "320 Machray", "Steve Stevenson","Steve@steve.com","999-9999","150 EITC","10:00:00")
        record = db.getSingleClass(username, className)
        self.assertEqual("A01", record.section)
        self.assertEqual("320 Machray", record.classroom)
        self.assertEqual("Steve Stevenson", record.prof_Name)
        self.assertEqual("Steve@steve.com", record.prof_Email)
        self.assertEqual("999-9999", record.prof_Phone)
        self.assertEqual("150 EITC", record.prof_Office)
        self.assertIn("10:00:00", record.prof_Hours)






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


if __name__ == '__main__':
    unittest.main()
