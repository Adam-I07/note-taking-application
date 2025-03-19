import notes_application.view_notes
import notes_application.notes_validation
import requests
from colorama import Fore

class DeleteNote():
    def __init__(self):
        self.view_notes_instance = notes_application.view_notes.ViewNotes()
        self.notes_validation_instance = notes_application.notes_validation.NotesValidation()

    def delete_note(self, user_logged_in):
        url_display = f'http://127.0.0.1:8000/notes/user/specific/{user_logged_in}'
        response_display = requests.get(url_display)
        data = response_display.json()
        try:
            if data['detail'] == "User with ID does not have notes":
                print("---------------------")
                print(Fore.YELLOW + "You currently have no notes created, first create notes to delete them!" + Fore.WHITE)
                return
        except:
            pass
        self.notes_validation_instance.create_table(data)
        delete = self.notes_validation_instance.select_note_to_delete(user_logged_in)
        if delete == 'back':
            return
        