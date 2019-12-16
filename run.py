#!/usr/bin/env
from user import user

def create_user(aname,lname,phone,email):
    '''
    Function to create a new user
    '''
    new_user = user(aname,lname,phone,email)
    return new_user

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def find_user(number):
    '''
    Function that finds a user by number and returns the user
    '''
    return user.find_by_number(number)

def check_existing_users(number):
    '''
    Function that check if a user exists with that number and return a Boolean
    '''
    return user.user_exist(number)

def display_users():
    '''
    Function that returns all the saved users
    '''
    return user.display_users()

def main():
    print("Hello Welcome to the password locker!")
    user_name = input()

    print(f"Hello {user_name}. Please Log in to your account")
    print('\n')

    while True:
        print("cc- create a new user account, dc - login into your account (if you already have a password locker account), fc - Enter the account you want to search for, EX - exit from password locker")
        short_code = input().lower()
        if short_code == 'cc':
            print("New user")
            print("-"*10)

            print ("Account name ....")
            a_name = input()

            print("Last name ...")
            l_name = input()

            print("Phone number ...")
            p_number = input()

            print("Email address ...")
            e_address = input()
            save_users(create_user(a_name,l_name,p_number,e_address)) # create and save new user.
            print ('\n')
            print(f"New user {a_name} {l_name} created")
            print ('\n')

        elif short_code == 'dc':
            if display_users():
                print("login into your account")
                print('\n')
                for user in display_users():
                   print("{user.account_name} {user.last_name} .....{user.phone_number}")
                   print('\n')
            else:
                print('\n')
                print("You dont seem to have any account saved yet")
                print('\n')

        elif short_code == 'fc':
            print("Enter the account you want to search for")
            search_number = input()
            if check_existing_users(search_number):
                search_user = find_user(search_number)
                print(f"{search_user.account_name} {search_user.last_name}")
                print('-' * 20)

                print(f"Phone number.......{search_user.phone_number}")
                print(f"Email address.......{search_user.email}")
            else:
                    print("That account does not exist")
        elif short_code == "ex":
            print("exit from password locker")
            break
        else:
                print("Please use the short codes")

if __name__ == '__main__':
    main()