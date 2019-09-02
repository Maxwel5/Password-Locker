#!/usr/bin/env python3.6
from password import User

def create_user(fname,lname,username,password):
    '''
    Function to create a new user
    '''
    new_user = User(fname,lname,username,password)
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

def find_user(username):
    '''
    Function that finds the user by username and returns the user
    '''
    return users.find_by_username(username)

def check_existing_users(username):
    '''
    Function that check if a user exists with that usename and return a Boolean
    '''
    return User.user_exist(username)

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

def main():
    print("Hi! This is your password locker. Your name please")
        
    user_name = input()

    print(f"Hi {user_name}. Do what you like")

    print('\n')

    while True:
        print("Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, ex -exit the contact list ")

        short_code = input().lower()

        if short_code == 'cc':
            print("New User")
            print("-"*5)

            print ("First name ...")
            f_name = input()

            print ("Last name ...")
            l_name = input()

            print ("User name ...")
            u_name = input()

            print ("password ...")
            pwd = input()

            save_users(create_user(f_name,l_name,u_name,pwd))

            print ('\n')
            print(f"New User {f_name} {l_name} created")
            print ('\n')


        elif short_code == 'dc':

            if display_users():
                print("This is a group of users available")
                print('\n')

                for user in display_users():
                    print(f"{user.first_name} {user.last_name} .....{user.user_name}")
                print('\n')

            else:
                print('\n')
                print("No saved users")
                print('\n')

        elif short_code == 'fc':
            
            print("Enter user name you want to find")
                    
            search_username = input()
            if check_existing_users(search_username):

                search_user = find_user(search_username)

                print(f"{search_user.first_name} {search_user.last_name}")

                print('-' * 10) 

                print(f"username.......{search_user.user_name}")

                print(f"password.......{search_user.password}")

            else:
                print("The contact does not exist")

        elif short_code == "ex":
            
            # if able to execute the short_code
                print("bye-bye .......")
                break
        else:
                print("I mean, didn't get it. Can you please use the short codes")

if __name__ == '__main__':
    main()


    

