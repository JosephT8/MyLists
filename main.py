"""
Controls the user interaction with the program.
"""

class Interface(object):
    def __init__(self):
        self.login()
    def login(self):
        username = input("What is your username? If new type 'new': ")
        password = input("What is your password?: ")
