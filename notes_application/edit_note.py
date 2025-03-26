import notes_application.notes_validation
from colorama import Fore
from datetime import datetime
import requests


class EditNote():
    def __init__(self):
        self.notes_validation_instance = notes_application.notes_validation.NotesValidation()

    def edit_note(self, logged_in_user):
        self.edit_note_menu()
        url_display = f'http://127.0.0.1:8000/notes/user/specific/{logged_in_user}'
        response_display = requests.get(url_display)
        data = response_display.json()
        try:
            if data['detail'] == "User with ID does not have notes":
                print(Fore.YELLOW + "You currently have no notes created, first create notes to edit them!" + Fore.WHITE)
                return
        except:
            pass
        print(Fore.YELLOW + "Info: when you select edit a secton of the note you have to enter new input previous input will be removed." + Fore.WHITE)
        self.notes_validation_instance.create_table(data)
        notes = self.notes_validation_instance.select_note_to_edit(logged_in_user)
        if notes == 'back':
            return
        note = {"id" : "", "user_id" : "", "title" : "", "content" : "", "tags" : "", "created_at" : "", "updated_at": ""}
        for n in notes:
            note['id'] = n[0]
            note['user_id'] = n[1]
            note['title'] = n[2]
            note['content'] = n[3]
            note['tags'] = n[4]
            note['created_at'] = n[5]
            note['updated_at'] = n[6]
        title = self.edit_title(note['title'])
        note['title'] = title
        content = self.edit_content(note['content'])
        note['content'] = content
        tags = self.edit_tags(note['tags'])
        note['tags'] = tags
        date_format = '%d-%m-%Y %H:%M:%S'
        current_date_time = datetime.now().strftime(date_format)
        note['updated_at'] = current_date_time
        confirmation = self.notes_validation_instance.confirm_edit()
        if confirmation == True:
            url_edit = f"http://127.0.0.1:8000/notes/edit"
            response_edit = requests.put(url_edit, json=note)
            data = response_edit.json()
            print("---------------------")
            if data == "updated note":
                print(Fore.GREEN + "Note Successfully Edited!" + Fore.WHITE)
                return
            else:
                print(Fore.RED + "Error could not update note!" + Fore.WHITE)
        else:
            return

    def edit_note_menu(self):
        print("---------------------")
        print("Edit Note")
        print("---------------------")
        
    def edit_title(self, title):
        while True:
            user_input = input(f"The current title entered is '{title}' would you like to edit and enter a new title? (y/n): ")
            if user_input.lower() == 'y':
                new_title = self.notes_validation_instance.title_validation()
                return new_title
            elif user_input.lower() == 'n':
                return title
            else:
                print(Fore.RED + "Invalid input, try again!" + Fore.WHITE)
    
    def edit_content(self, content):
        while True:
            print(f"The current content entered is '{content}'")
            user_input = input(f"Would you like to edit and enter new content? (y/n): ")
            if user_input.lower() == 'y':
                new_content = self.notes_validation_instance.content_validation()
                return new_content
            elif user_input.lower() == 'n':
                return content
            else:
                print(Fore.RED + "Invalid input, try again!" + Fore.WHITE)

    def edit_tags(self, tags):
        while True:
            user_input = input(f"The current tags inputted are {tags} would you like edit and enter new tags? (y/n): ")
            if user_input.lower() == 'y':
                new_tags = self.notes_validation_instance.tags_validation()
                return new_tags
            elif user_input.lower() == 'n':
                return tags
            else:
                print(Fore.RED + "Invalid input, try again!" + Fore.WHITE)