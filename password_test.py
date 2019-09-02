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
            User.user_list = []

    def test_save_multiple_user(self):
            '''
            test_save_multiple_user this check if we are able to save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("Test","user","Max","9876") 
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        '''
        test_delete_user to try if we can delete a user from our user list
        '''
        self.new_user.save_user()
        test_user = User("Test","user","Max","9876")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)

    def delete_user(self):

        '''
        delete_user method removes/deletes a saved user from the user_list
        '''

        User.user_list.remove(self)
    
    def test_find_user_by_username(self):
        '''
        test to check if we can find a user by username and display information
        '''

        self.new_user.save_user()
        test_user = User("Test","user","Max","9876") 
        test_user.save_user()

        found_user = User.find_by_username("Max")

        self.assertEqual(found_user.password,test_user.password)
    
    @classmethod
    def find_by_username(cls,username):
        '''
        Method that takes in a username and returns a user that matches that username.

        Args:
            username: Username to search for
        Returns :
            User of person that matches the username.
        '''

        for contact in cls.contact_list:
            if contact.phone_number == number:
                return contact
    
    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = User("Test","user"," "," ") 
        test_user.save_user()

        user_exists = User.user_exist(" ")

        self.assertTrue(user_exists)

    @classmethod
    def user_exist(cls,number):
        '''
        Method that checks if the user exists from the user list.
        Args:
            username: Username to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.user_name == username:
                    return True

        return False

    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''

        self.assertEqual(User.display_users(),User.user_list)

if __name__ ==  '__main__':
    unittest.main()

