import unittest
import db
import pyodbc


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
                    r'Trusted_Connection=yes'
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
        self.assertIn(username, result)

    '''
    Test passes if user is sucessfully inserted into the db (asserting that user appears in retrieved record)
    Mock user is removed at the end of the test
    '''

    def test_removeUser(self):
        username = "test"
        password = "testing"
        db.createAccount(username, password)
        # remove user
        db.removeUser(username)
        result = db.getAllUsers()
        self.assertNotIn(username, result)

    def test_createAccount(self):
        username = "test"
        password = "testing"
        db.createAccount(username, password)
        # retrieve the mock user from the db
        result = db.getUser(username)
        self.assertIn(username, result)
        #remove user
        db.removeUser(username)


if __name__ == '__main__':
    unittest.main()
