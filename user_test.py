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



if __name__ == '__main__':
    unittest.main()