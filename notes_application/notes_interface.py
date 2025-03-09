from colorama import Fore
import notes_application.add_note
import notes_application.view_notes

class NotesInterface():
    def __init__(self):
        self.logged_in_user = None

    def logged_in(self, user):
        self.logged_in_user = user
        self.menu_options()
        while True:
            user_option = input("Enter the number assosicated with the option you would like to invoke: ")
            if user_option == "1":
                self.add_note_instance = notes_application.add_note.AddNote()
                self.add_note_instance.add_new_note(self.logged_in_user)
                self.menu_options()
            elif user_option == "2":
                print("Edit Note")
            elif user_option == "3":
                print("View Notes")
                self.view_note_instance = notes_application.view_notes.ViewNotes()
                self.view_note_instance.view_note(self.logged_in_user)
                self.menu_options()
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

        