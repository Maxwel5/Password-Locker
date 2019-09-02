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
         