import unittest
from password import User

class TestIUser(unittest.TestCase):
    '''
    This tests class that defines test cases for the user class characteristics.
    Args:
    unittest.TestCase:TestCase class is a subclass for creating test cases
    '''

    def setUp(self):
        '''
        A method that runs before each test cases.
        '''
        self.new_user = User("Maxwel","Wafula","Max","9876")
