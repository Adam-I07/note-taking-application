import notes_application.notes_validation
import requests
from colorama import Fore

class ViewNotes():
    def __init__(self):
        self.notes_validation_instance = notes_application.notes_validation.NotesValidation()

    def view_note(self, logged_in_user):
        self.view_notes_title()
        url = f'http://127.0.0.1:8000/notes/user/specific/{logged_in_user}'
        response = requests.get(url)
        data = response.json()
        try:
            if data['detail'] == "User with ID does not have notes":
                print(Fore.YELLOW + "You currently have no notes created, first create notes to view them!" + Fore.WHITE)
                return
        except:
            pass
        self.notes_validation_instance.create_table(data)

    def view_notes_title(self):
        print("---------------------")
        print("All Notes:")
        print("---------------------")