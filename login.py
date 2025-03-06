import user_validation
import user_json_handling
import notes_interface
from colorama import Fore

class Login():
    def __init__(self):
        self.user_validation_instance = user_validation.UserValidation()
        self.user_json_handling_instance = user_json_handling.UserJsonHandling()
    
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
            credentials_check = self.user_json_handling_instance.login(f"{username_inputted},{password_inputted}")
            credential_split = credentials_check.split(",")
            credentials_status = credential_split[0]
            extra_information = credential_split[1]
            if credentials_status == 'invalid':
                if extra_information == 'password':
                    print(Fore.RED + "Invalid Password! Try Again" + Fore.WHITE)
                
                if extra_information == 'username':
                    print(Fore.RED + "Invalid Username Try Again" + Fore.WHITE)
            else:
                print("---------------------")
                print(Fore.GREEN + "Successfully Logged In!" + Fore.WHITE)
                notes_interface_instance = notes_interface.NotesInterface()
                notes_interface_instance.logged_in(extra_information)
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