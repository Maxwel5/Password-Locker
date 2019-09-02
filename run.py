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
    return User.find_by_username(username)

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
