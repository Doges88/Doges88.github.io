# import packages
from getpass import getpass
import os
import sqlite3
import sys
import hashlib
from termcolor import colored

def main():
    
    con = sqlite3.connect("users.db")
    c = con.cursor()
    logged_in = False
    while not logged_in:
        new_user_or_log_in = input("Create a new user or log in N/L: ").lower()
        if new_user_or_log_in == "n":
            new_username = input("New username: ")
            new_password = getpass("New password: ")
            c.execute(f"INSERT INTO users VALUES ('{new_username}', '{hashlib.sha256(new_password.encode()).hexdigest()}')")
            con.commit()
            new_password=""
            
            print(colored(f"User {new_username} added!", 'green'))
        elif new_user_or_log_in == "l":
            username = input("Username: ")
            password = getpass("Password: ")
            c.execute(f"SELECT password FROM users WHERE username = '{username}'")
            real_password = c.fetchone()[0] 
            if hashlib.sha256(password.encode()).hexdigest() == real_password:
                logged_in = True
                print(colored(f"Welcome back, {username}", 'green'))
                password=""
               
            elif real_password == None:
                print(colored("User doesn't exist!", 'red'))
            else:
                print(colored("Wrong password!", 'red'))
    os.system("cls") # clear the screen after logging in
    while True:
        command = input(colored(f"{os.getcwd()}@{username} >>> ", 'blue'))
        if command == "exit":
            sys.exit("Quitting!")
        else:
            os.system(command)


main()

