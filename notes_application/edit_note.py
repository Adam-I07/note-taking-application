import notes_application.notes_validation 
import notes_application.notes_json_handling
from colorama import Fore
from datetime import datetime


class EditNote():
    def __init__(self):
        self.notes_validation_instance = notes_application.notes_validation.NotesValidation()
        self.notes_json_handling_instance = notes_application.notes_json_handling.NotesJsonHandling()

    def edit_note(self, logged_in_user):
        self.edit_note_menu()
        data = self.notes_json_handling_instance.get_display_user_notes(logged_in_user) 
        self.notes_validation_instance.create_table(data)
        note = self.notes_validation_instance.select_note_to_edit(logged_in_user)
        print(note)
        if note == 'back':
            return
        title = self.edit_title(note['title'])
        note['title'] = title
        content = self.edit_content(note['content'])
        note['content'] = content
        tags = self.edit_tags(note['tags'])
        note['tags'] = tags
        date_format = '%d/%m/%Y %H:%M:%S'
        current_date_time = datetime.now().strftime(date_format)
        note['updated_at'] = current_date_time
        confirmation = self.notes_validation_instance.confirm_edit()
        if confirmation == True:
            self.notes_json_handling_instance.edit_note(note) 
            print("---------------------")
            print(Fore.GREEN + "Note Successfully Edited!" + Fore.WHITE)
            return
        else:
            return

    def edit_note_menu(self):
        print("---------------------")
        print("Edit Note")
        print("---------------------")
        print(Fore.YELLOW + "Info: when you select edit a secton of the note you have to enter new input previous input will be removed." + Fore.WHITE)

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