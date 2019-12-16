import unittest # Importing the unittest module
from user import user # Importing the user class

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
            



if __name__ == '__main__':
    unittest.main()