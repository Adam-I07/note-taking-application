from colorama import Fore
import notes_application.notes_json_handling

class NotesValidation():
    def __init__(self):
        self.notes_json_handling_instance = notes_application.notes_json_handling.NotesJsonHandling()


    def confirm_save(self):
        while True:
            user_choice = input("Are you sure you would like to add this note (y/n): ")
            if user_choice.lower() == 'y':
                return True
            elif user_choice.lower == 'n':
                return False
            else:
                print(Fore.RED + "Invalid Input! You can only enter y for yes or n for no! Try Again!"+ Fore.WHITE)

    def title_validation(self):
        while True:
            user_input = input("Enter the title for you note: ")
            if user_input:
                title_validity = self.notes_json_handling_instance.check_title(user_input)
                if title_validity == False:
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
        return self.notes_json_handling_instance.get_next_id()

    def tags_validation(self):
        self.tag_options()
        tags = self.select_tags()
        selected_tags = self.return_tags(tags)
        print(selected_tags)


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


        

