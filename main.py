from colorama import Fore
import login
import register

class Start():
    def __init__(self):
        self.login_instance = login.Login()
        self.register_instance = register.Register()

    def start_program(self):
        self.start_program_options()
        while True:
            user_input = input("Enter the number assosicated with the option you would like to invoke: ")
            if user_input == "1":
                self.login_instance.login()
                self.start_program_options()
            elif user_input == "2":
                self.register_instance.start_registration()
                self.start_program_options()
            elif user_input == "3":
                self.exit_program()
            else:
                print(Fore.RED + "Invalid input only enter a number assosicated with a valid option presented!" + Fore.WHITE)

    def start_program_options(self):
        print("---------------------")
        print("Login or Register")
        print("---------------------")
        print("Options:")
        print("1. Login")
        print("2. Regsiter")
        print("3. Exit")
        print("---------------------")

    def exit_program(self):
        exit()

if __name__ == "__main__":
    start_app = Start()
    start_app.start_program()