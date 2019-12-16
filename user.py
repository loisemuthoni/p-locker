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