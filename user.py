#!/usr/bin/env python3.6
import pyperclip
from user import User

class User:
    # Providing user details

    def user_details(self,fname,lname,username,psword):

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
        detecting _user = Credential.detect_user(user_name,password)
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
        new_credential = Credential(user_name,account_name,password)
        return new_credential

    def save_credential(credential):
        '''
        Saving the new credentials in the function
        '''
        Credential.save_credential(credential)

    def view_credentials(user_name):
        '''
        Function to view the saved credentials by the user
        '''
        return Credential.view_credentials(user_name)
         