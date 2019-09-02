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

    def test_init(self):
        '''
        test_init checks for proper initializing of objects
        '''

    self.assertEqual(self.new_user.first_name,"Maxwel")
    self.assertEqual(self.new_user.last_name,"Wafulal")
    self.assertEqual(self.new_user.user_name,"Max")
    self.assertEqual(self.new_user.password,"9876")

if __name__ == '__main__':

