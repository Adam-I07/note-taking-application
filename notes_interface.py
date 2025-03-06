from colorama import Fore

class NotesInterface():
    def __init__(self):
        self.logged_in_user = None

    def logged_in(self, user):
        self.logged_in_user = user
        self.menu_options()
        while True:
            user_option = input("Enter the number assosicated with the option you would like to invoke: ")
            if user_option == "1":
                print("Add Notes")
            elif user_option == "2":
                print("Edit Note")
            elif user_option == "3":
                print("View Note")
            elif user_option == "4":
                print("Delete Note")
            elif user_option == "5":
                print("Filter Notes")
            elif user_option == "6":
                print("---------------------")
                print(Fore.GREEN + "Logged out" + Fore.WHITE)
                print("---------------------")
                return
        
    
    def menu_options(self):
        print("---------------------")
        print("Main Menu")
        print("---------------------")
        print("Options:")
        print("1. Add Note")
        print("2. Edit Note")
        print("3. View Note")
        print("4. Delete Note")
        print("5. Filter Notes")
        print("6. Logout")
        print("---------------------")

        