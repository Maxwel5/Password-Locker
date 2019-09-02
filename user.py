#!/usr/bin/env python3.6
import pyperclip
from user import User

class User:
    # Providing user details

    def create_user(self,fname,lname,username,psword):

        '''
        Improvised function for crearing new user details 
        '''
        new_user = User(self,fname,lname,username,psword)
        return new_user

    def save_user(user):
        '''
        Function to save/store new user details
        '''
        User.save_user

    def justify_user(user_name,password):
        '''
        Functin to identify the actual account user
        '''
        detecting_user = Credential.detect_user(user_name,password)
        return detecting_user

    def generate_password():
        '''
        Function to generate self_password
        '''
        generate_password = Credential.generate_password()
        return generate_password

class Credentials:
    # Credentials details
    def credential_details(user_name,account_name,password):
        '''
        Credential function
        '''
        new_credential = Credential(user_name,site_name,account_name,password)
        return new_credential

    def save_credential(credential):
        '''
        Saving the new credentials in the function
        '''
        Credential.save_credential(credential)

    def del_credential(credential):
        '''
        Function to delete credentials that are not needede in the app.
        '''
        credential.delete_credential()

    def view_credentials(user_name):
        '''
        Function to view the saved credentials by the user
        '''
        return Credential.view_credentials(user_name)

    def duplicate_credential(site_name):
        '''
        Function that duplicates credentials details to the clipboard
        '''
        return Credentials.duplicate_credential(site_name)

    def main():
        print("Hi! This is your password locker. Your name please")
            user_name = input()

            print(f"Hi {user_name}. Do what you like")

            print('\n')

            while True:
                print("use this short codes : cs - create a new user, vt - view credential, gp - generate password, dt - duplicate credential")

                short_code = input().lower()

                if short_code == 'cs':
                    print("New User")
                    print("-"*5)

                    print ("First name ...")
                    f_name = input(Enter your first name)

                    print ("Last name ...")
                    f_name = input(Enter your last name)

                    print ("User name ...")
                    f_name = input(Enter username)

                    print ("password ...")
                    pwd = input(password)
                            break
                
         