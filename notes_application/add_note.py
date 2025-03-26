import notes_application.notes_validation
from datetime import datetime
from colorama import Fore
import requests

class AddNote():
    def __init__(self):
        self.notes_validation_instance = notes_application.notes_validation.NotesValidation()

    def add_new_note(self, user_id):
        note = {"id" : "", "user_id" : "", "title" : "", "content" : "", "tags" : "", "created_at" : "", "updated_at": ""}
        note["id"] = self.notes_validation_instance.get_next_id()
        note["user_id"] = int(user_id)
        self.add_note_title()
        title = self.notes_validation_instance.title_validation()
        note["title"] = title
        content = self.notes_validation_instance.content_validation()
        note["content"] = content
        tags = self.notes_validation_instance.tags_validation()
        note["tags"] = tags
        date_format = '%d-%m-%Y %H:%M:%S'
        current_date_time = datetime.now().strftime(date_format)
        note["created_at"] = current_date_time
        note["updated_at"] = current_date_time
        confirmation = self.notes_validation_instance.confirm_save()
        if confirmation == True:
            url = "http://127.0.0.1:8000/notes/create"
            response_edit = requests.post(url, json=note)
            data = response_edit.json()
            print("---------------------")
            if data == "created note":
                print(Fore.GREEN + "Note Successfully Saved!" + Fore.WHITE)
                return
            else:
                print(Fore.RED + "Error could add note!" + Fore.WHITE)
        else:
            return


    def add_note_title(self):
        print("---------------------")
        print("Add Note")
        print("---------------------")