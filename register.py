import user_validation
import user_json_handling
from colorama import Fore

class Register():
    def __init__(self):
        self.user_validation_instance = user_validation.UserValidation()
        self.user_json_handling_instance = user_json_handling.UserJsonHandling()

    def start_registration(self):
        print("---------------------")
        print("Register")
        print("---------------------")
        username_inputted = self.username_input()
        if username_inputted == 'b':
            return
        password_inputted = self.password_input()
        if password_inputted == 'b':
                return
        self.user_json_handling_instance.register_user(f"{username_inputted},{password_inputted}")
        print("---------------------")
        print(f"{username_inputted} successfully registered!")
        return

    def password_input(self):
        while True:
            user_input = input("Password, enter 'b' to return to main menu: ")
            has_input_error = False
            has_length_error = False
            has_uppercase_error = False
            has_lowercase_error = False
            has_number_error = False
            has_special_character_error = False

            input_check = self.user_validation_instance.check_input(user_input)
            if input_check is False: has_input_error = True

            if has_input_error is False:
                length_check = self.user_validation_instance.check_password_length(user_input)
                if length_check is False: has_length_error = True
            
            if has_input_error is False and has_length_error is False:
                uppercase_check = self.user_validation_instance.check_password_uppercase(user_input)
                if uppercase_check is False: has_uppercase_error = True

            if has_input_error is False and has_length_error is False and has_uppercase_error is False:
                lowercase_check = self.user_validation_instance.check_password_lowercase(user_input)
                if lowercase_check is False: has_lowercase_error = True 
            
            if has_input_error is False and has_length_error is False and has_uppercase_error is False and has_lowercase_error is False:
                numerical_check = self.user_validation_instance.check_password_numerical(user_input)
                if numerical_check is False: has_number_error = True
            
            if has_input_error is False and has_length_error is False and has_uppercase_error is False and has_lowercase_error is False and has_number_error is False:
                special_char_check = self.user_validation_instance.check_password_special_character(user_input)
                if special_char_check is False: has_special_character_error = True

            if user_input.lower() == 'b':
                return 'b'
            elif has_input_error is True:
                print(Fore.RED + "You must input a valid password!" + Fore.WHITE)
            elif has_length_error is True:
                print(Fore.RED + "Password must be a minimum of 7 letters long!" + Fore.WHITE)
            elif has_uppercase_error is True:
                print(Fore.RED + "You must have atleast one uppercase letter in the password" + Fore.WHITE)
            elif has_lowercase_error is True:
                print(Fore.RED + "You must have atleast one lowercase letter in the password" + Fore.WHITE)
            elif has_number_error is True:
                print(Fore.RED + "You must have atleast one number in the password" + Fore.WHITE)
            elif has_special_character_error is True:
                print(Fore.RED + "You must have atleast one special character in the password such as: / ; ! ?" + Fore.WHITE)
            else:
                return user_input


    def username_input(self):
        while True:
            user_input = input("Username, enter 'b' to return to main menu: ")
            input_to_check = user_input.lower()
            has_input_error = False
            already_exists_error = False
            length_error = False

            input_check = self.user_validation_instance.check_input(input_to_check)
            if input_check is False: has_input_error = True

            if has_input_error is False:
                username_check = self.user_validation_instance.check_username_exists(input_to_check)
                if username_check is True: already_exists_error = username_check

            if has_input_error is False and already_exists_error is False:
                username_length = self.user_validation_instance.check_username_length(input_to_check)
                if username_length is False: length_error = True

            if user_input.lower() == 'b':
                return 'b'
            elif has_input_error is True:
                print(Fore.RED + "You must input a valid username!" + Fore.WHITE)
            elif already_exists_error is True:
                print(Fore.RED + "Username already exists try again!" + Fore.WHITE)
            elif length_error is True:
                print(Fore.RED + "Username must be longer than 4 letters, 5 minimum!" + Fore.WHITE)
            else:
                return input_to_check

