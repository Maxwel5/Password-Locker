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