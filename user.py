import pyperclip

class user:
    user_list = []
    def save_user(self):


        user.user_list.append(self)

    def __init__(self,account_name,last_name,phone_number,email):

         
          
        self.account_name = account_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        user.user_list.remove(self)

    @classmethod
    def find_by_number(cls,number):
        
        for user in cls.user_list:
            if user.phone_number == number:
                return user

    @classmethod
    def user_exist(cls,number):
       
        for user in cls.user_list:
            if user.phone_number == number:
                    return True

        return False

    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list

    @classmethod
    def copy_email(cls,number):
        user_found = user.find_by_number(number)
        pyperclip.copy(user_found.email)