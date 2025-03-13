import notes_application.notes_validation 
import notes_application.filter_notes_backend
from colorama import Fore

class FilterNotes():
    def __init__(self):
        self.notes_validation_instance = notes_application.notes_validation.NotesValidation()
        self.filter_notes_backend_instance = notes_application.filter_notes_backend.FilterNotesBackend()

    def filter_note(self, logged_in_user):
        self.filter_note_menu()
        while True:
            user_input = input("Enter the numerical value assosciated with the aciton you would like to invoke: ")
            if user_input == "1":
                self.filter_date(logged_in_user)
                self.filter_note_menu()
            elif user_input == "2":
                self.filter_notes_backend_instance.filter_by_content_title(logged_in_user)
                self.filter_note_menu()
            elif user_input == "3":
                self.filter_notes_backend_instance.filter_by_tags(logged_in_user)
                self.filter_note_menu()
            elif user_input == "4":
                return
            else:
                print(Fore.RED + "You have entered an input! Try again!" + Fore.WHITE)

    def filter_note_menu(self):
        print("---------------------")
        print("Filter Note")
        print("---------------------")
        print("Options:")
        print("1. Filter by Date")
        print("2. Filter by Content or Title")
        print("3. Filter by Tags")
        print("4. Go Back")
        print("---------------------")
    
    def filter_date(self, logged_in_user):
        self.filter_date_menu()
        while True:
            user_input = input("Enter the numerical value assosciated with the action you would like to invoke: ")
            print("---------------------")
            if user_input == "1":
                self.filter_notes_backend_instance.select_day(logged_in_user)
                self.filter_date_menu()
            elif user_input == "2":
                self.filter_notes_backend_instance.select_month(logged_in_user)
                self.filter_date_menu()
            elif user_input == "3":
                self.filter_notes_backend_instance.select_year(logged_in_user)
                self.filter_date_menu()
            elif user_input == "4":
                return
            else:
                print(Fore.RED + "You have entered an input! Try again!" + Fore.WHITE)

    def filter_date_menu(self):
        print("---------------------")
        print("Filter by Date")
        print("---------------------")
        print("Options:")
        print("1. Filter by Day")
        print("2. Filter by Month")
        print("3. Filter by Year")
        print("4. Go Back")
        print("---------------------")