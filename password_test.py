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

    def test_save_user(self):
        '''
        test_save_user test case to ensure if the user object is saved into
        the user list
        '''
        self.new_user.save_user() 
        self.assertEqual(len(User.user_list),1)

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user
        objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("Test","user","Max","9876") 
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def tearDown(self):
            '''
            tearDown method that clear up after each test case has run.
            '''
            Contact.contact_list = []

    def test_save_multiple_contact(self):
            '''
            test_save_multiple_contact to check if we can save multiple contact
            objects to our contact_list
            '''
            self.new_contact.save_contact()
            test_contact = Contact("Test","user","0712345678","test@user.com") # new contact
            test_contact.save_contact()
            self.assertEqual(len(Contact.contact_list),2)

if __name__ ==  '__main__':
    unittest.main()

