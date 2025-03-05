import user_json_handling
class UserValidation():
    def __init__(self):
        self.user_json_handling_instance = user_json_handling.UserJsonHandling()

    def check_input(self, input):
        if input:
            return True
        else:
            return False
    
    def check_password_length(self, input):
        if len(input) >= 7:
            return True
        else:
            return False
        
    def check_password_uppercase(self, input):
        input_split = [i for i in input]
        for letter in input_split:
            if letter.isupper():
                return True
        return False
    
    def check_password_lowercase(self, input):
        input_split = [i for i in input]
        for letter in input_split:
            if letter.islower():
                return True
        return False
    
    def check_password_numerical(self, input):
        input_split = [i for i in input]
        for letter in input_split:
            if letter.isdigit():
                return True
        return False

    def check_password_special_character(self, input):
        special_characters = ['#', '$', '%', '&', '!', '?', '@', '^', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\', ';', ':', '"', "'", '<', '>', ',', '.', '/', '~', '`']
        input_split = [i for i in input]
        for letter in input_split:
            if letter in special_characters:
                return True
        return False

    def check_username_exists(self, input):
        check = self.user_json_handling_instance.check_username(input)
        if check is True:
            return True
        else:
            return False
    
    def check_username_length(self, input):
        if len(input) > 4:
            return True
        else:
            return False 
        