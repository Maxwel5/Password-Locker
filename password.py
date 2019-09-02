#!/usr/bin/env python3.6

class User:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        self.username = uname
        self.password = psword

    def printname(self):
        print(self.firstname, self.lastname, self.username, self.password)

class Credential(User):
    def __init__(self, fname, lname, uname, psword ):
        super().__init__(fname, lname, uname, psword)
        self.credential = credential

    def hi(self):
        print("Hi", self.firstname, self.lastname, "to your acount", self.username, self.password)
    
    def save_user(self):
        '''
        Function to save/store new user details
        '''
        User.save_list.append(self)

    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list






                
         