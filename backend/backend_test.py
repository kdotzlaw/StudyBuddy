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
            conn = (r'Driver=SQL Server;'
                    r'Server=(local);'
                    r'Database=StudyBuddy;'
                    r'username=SA;'
                    r'password=dbtools.IO'
                    )
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
        #db.removeUser(username)
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
    def test_getClasses(self):
        username = "katDot"
# Class Tests
    #def test_getClasses(self):

    def test_ClassId(self):
        username = 'katDot'
        className = 'Comp 4350'
        record = db.getClassID(username,className)
        self.assertEqual(3,record)

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
