import user_handling.user_validation as user_validation
import notes_application.notes_interface as notes_interface
from colorama import Fore
import requests

class Login():
    def __init__(self):
        self.user_validation_instance = user_validation.UserValidation()
    
    def login(self):
        print("---------------------")
        print("Login")
        print("---------------------")
        while True:
            username_inputted = self.username_input()
            if username_inputted == 'b':
                return
            password_inputted = self.password_input()
            if password_inputted == 'b':
                return
            
            credentials = {"username": f"{username_inputted}", "password": f"{password_inputted}"}
            url = f"http://127.0.0.1:8000/auth/check/login"
            response = requests.post(url, json=credentials)
            check = response.json()
            check_split = check['detail'].split(" ")
            if check_split[0] == 'Invalid':
                if check_split[1] == 'password':
                    print(Fore.RED + "Invalid Password! Try Again" + Fore.WHITE)
                if check_split[1] == 'username':
                    print(Fore.RED + "Invalid Username Try Again" + Fore.WHITE)
            else:
                print("---------------------")
                print(Fore.GREEN + "Successfully Logged In!" + Fore.WHITE)
                notes_interface_instance = notes_interface.NotesInterface()
                notes_interface_instance.logged_in(check_split[1])
                return


    def password_input(self):
        while True:
            user_input = input("Password, enter 'b' to return to main menu: ")
            has_input_error = False

            input_check = self.user_validation_instance.check_input(user_input)
            if input_check is False: has_input_error = True

            if user_input.lower == 'b':
                return 'b'
            elif has_input_error is True:
                print(Fore.RED + "You must input a valid password!" + Fore.WHITE)
            else:
                return user_input


    def username_input(self):
        while True:
            user_input = input("Username, enter 'b' to return to main menu: ")
            input_to_check = user_input.lower()
            has_input_error = False

            input_check = self.user_validation_instance.check_input(input_to_check)
            if input_check is False: has_input_error = True

            if user_input.lower == 'b':
                return 'b'
            elif has_input_error is True:
                print(Fore.RED + "You must input a valid username!" + Fore.WHITE)
            else:
                return input_to_check