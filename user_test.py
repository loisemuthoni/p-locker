import unittest # Importing the unittest module
from user import user # Importing the user class
import pyperclip

class TestUser(unittest.TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = user("Loise","Peter","0712345678","loise@ms.com") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.account_name,"Loise")
        self.assertEqual(self.new_user.last_name,"Peter")
        self.assertEqual(self.new_user.phone_number,"0712345678")
        self.assertEqual(self.new_user.email,"loise@ms.com")

    def test_save_user(self):
        
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(user.user_list),1)


    def test_save_multiple_user(self):
           
        self.new_user.save_user()
        test_save_user = user("Test","user","0712345678","test@user.com") # new user
        test_user.save_user()
        self.assertEqual(len(user.user_list),2)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            user.user_list = []

    def test_save_multiple_user(self):
           
        self.new_user.save_user()
        test_user = user("Test","user","0712345678","test@user.com") # new user
        test_user.save_user()
        self.assertEqual(len(user.user_list),2)

    def test_delete_user(self):
           
        self.new_user.save_user()
        test_user = user("Test","user","0712345678","test@user.com") # new user
        test_user.save_user()

        self.new_user.delete_user()# Deleting a user object
        self.assertEqual(len(user.user_list),1)

    def test_find_user_by_number(self):
        '''
        test to check if we can find a user by phone number and display information
        '''

        self.new_user.save_user()
        test_user = user("Test","user","0711223344","test@user.com") 
        test_user.save_user()

        found_user = user.find_by_number("0711223344")

        self.assertEqual(found_user.email,test_user.email)

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = user("Test","user","0711223344","test@user.com")
        test_user.save_user()

        user_exists = user.user_exist("0711223344")

        self.assertTrue(user_exists)

    def test_display_all_users(self):
        '''
        method that returns a list of all user saved
        '''

        self.assertEqual(user.display_users(),user.user_list)

    def test_copy_email(self):
        '''
        Test to confirm that we are copying the email address from a found user
        '''

        self.new_user.save_user()

        user.copy_email("0712345678")

        self.assertEqual(self.new_user.email,pyperclip.paste())

       
            



if __name__ == '__main__':
    unittest.main()