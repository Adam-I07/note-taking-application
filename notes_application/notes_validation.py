from colorama import Fore
from tabulate import tabulate
import requests

class NotesValidation():
    def __init__(self):
        pass

    def select_note_to_edit(self, user_logged_in):
        url = f'http://127.0.0.1:8000/notes/existing/user/{user_logged_in}'
        response = requests.get(url)
        notes_can_be_edited = response.json()
        while True:
            user_input = input("Enter the id of the note you would like to edit, or 'b' to go back to Main Menu: ")
            check_input_type = self.check_user_input_type(user_input)
            if check_input_type == "int":
                if int(user_input) in notes_can_be_edited:
                    url_edit = f'http://127.0.0.1:8000/notes/existing/selected/note/{int(user_input)}'
                    response_edit = requests.get(url_edit)
                    note = response_edit.json()
                    return note
                else:
                    print(Fore.RED + "You have entered an invalid ID! Try again!" + Fore.WHITE)
            else:
                if user_input.lower() == 'b':
                    return "back"
                else:
                    print(Fore.RED + "Invalid input you can only enter a valid note ID or 'b' to go back! Try again!" + Fore.WHITE)
        
    def confirm_edit(self):
        while True:
            user_choice = input("Are you sure you would like to edit this note (y/n): ")
            if user_choice.lower() == 'y':
                return True
            elif user_choice.lower() == 'n':
                return False
            else:
                print(Fore.RED + "Invalid Input! You can only enter y for yes or n for no! Try Again!"+ Fore.WHITE)

    def select_note_to_delete(self, user_logged_in):
        url = f'http://127.0.0.1:8000/notes/existing/user/{user_logged_in}'
        response = requests.get(url)
        notes_can_be_deleted_id = response.json()
        while True:
            user_input = input("Enter the id of the note you would like to delete, or 'b' to go back to Main Menu: ")
            check_input_type = self.check_user_input_type(user_input)
            if check_input_type == "int":
                if int(user_input) in notes_can_be_deleted_id:
                    self.confirm_delete(user_input)
                    return
                else:
                    print(Fore.RED + "You have entered an invalid ID! Try again!" + Fore.WHITE)
            else:
                if user_input.lower() == 'b':
                    return "back"
                else:
                    print(Fore.RED + "Invalid input you can only enter a valid note ID or 'b' to go back! Try again!" + Fore.WHITE)
    
    def confirm_delete(self, delete_note_id):
        while True:
            user_final_choice = input(f"Are you sure you would permanently delete note {delete_note_id}? (y/n) ")
            if user_final_choice.lower() == 'y':
                url = f'http://127.0.0.1:8000/notes/remove/{delete_note_id}'
                response = requests.delete(url)
                delete_response = response.json()
                if delete_response == "Successfully Deleted":
                    print(Fore.GREEN + f"{delete_note_id} has been deleted successfully!" + Fore.WHITE)
                    return
                else:
                    print(Fore.RED + "Error! Unable to Delete Note!"+ Fore.WHITE)
            elif user_final_choice.lower() == 'n':
                return
            else:
                print(Fore.RED + "Invalid Input, you can only enter y for yes or n for no! Try Again!" + Fore.WHITE)

    def confirm_save(self):
        while True:
            user_choice = input("Are you sure you would like to add this note (y/n): ")
            if user_choice.lower() == 'y':
                return True
            elif user_choice.lower() == 'n':
                return False
            else:
                print(Fore.RED + "Invalid Input! You can only enter y for yes or n for no! Try Again!"+ Fore.WHITE)

    def title_validation(self):
        while True:
            user_input = input("Enter the title for you note: ")
            if user_input:
                url_edit = f'http://127.0.0.1:8000/notes/existing/check/title/{user_input}'
                response_edit = requests.get(url_edit)
                response = response_edit.json()
                if response == False:
                    return user_input
                else:
                    print("---------------------")
                    print(Fore.RED + "Title already exists, try again!" + Fore.WHITE)
                    print("---------------------")
            else:
                print(Fore.RED + "You must enter an input for the title! Try Again!" + Fore.WHITE)

    def content_validation(self):
        while True:
            user_input = input("Enter the content for you note: ")
            if user_input:
                return user_input
            else:
                print(Fore.RED + "You must enter an input for the title! Try Again!" + Fore.WHITE)

    def get_next_id(self):
        url_edit = 'http://127.0.0.1:8000/notes/next/available/id'
        response_edit = requests.get(url_edit)
        response = response_edit.json()
        return response

    def tags_validation(self):
        self.tag_options()
        tags = self.select_tags()
        selected_tags = self.return_tags(tags)
        return selected_tags

    def select_tags(self):
        tags = []
        while True:
            user_input = input("Enter the numerical value assosciated with the tag you would like to select or 's' to save your tag choices and go back:")
            check_type = self.check_user_input_type(user_input)
            if check_type == "int":
                if int(user_input) > 0 and int(user_input) < 15:
                    tags.append(user_input)
                else:
                    print(Fore.RED + "You must input a valid tag number from the list provided! Try Again" + Fore.WHITE)
            elif check_type == "string":
                if user_input.lower() == 's':
                    validity = self.check_if_tags(tags)
                    if validity == True:
                        return tags
                    elif validity == "no":
                        print(Fore.RED + "You must select atleast 1 Tag! Try again!" + Fore.WHITE)
                else:
                    print(Fore.RED + "Invalid Input, try again!" + Fore.WHITE)
            else:
                print(Fore.RED + "Invalid Input, try again!" + Fore.WHITE)
    
    def check_user_input_type(self, input):
        try:
            int(input)
            return "int"
        except:
            return "string"
    
    def check_if_tags(self, tags):
        if tags:
            return True
        else:
            return "no"

    def tag_options(self):
        tag_options = ["work", "personal", "school", "shopping", "travel", "health", "finance", "ideas", "recipes", "urgent", "important", "todo", "done", "in-progress"]
        print("---------------------")
        num = 0
        print("Tags:")
        for tag in tag_options:
            num = num + 1
            print(f"{num}. {tag}")
        print("---------------------")

    def return_tags(self, tags):
        tag_options = ["work", "personal", "school", "shopping", "travel", "health", "finance", "ideas", "recipes", "urgent", "important", "todo", "done", "in-progress"]
        to_return = []
        for tag in tags:
            index = int(tag) - 1
            to_return.append(tag_options[index])
        return to_return

    def create_table(self, data):
        try:
            print(tabulate(data, headers='keys', tablefmt='grid'))
        except:
            print(Fore.RED + "Error, Could not create table from given data!" + Fore.WHITE)

