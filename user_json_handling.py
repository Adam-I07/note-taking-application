import json
import password_hashing

class UserJsonHandling():
    def __init__(self):
        self.password_hashing_instance = password_hashing.PasswordHashing()
        self.user_data = []

    def get_user_data(self):
        try: 
            self.user_data.clear()
        except:
            pass
        with open('users.json') as f:
            self.user_data = json.load(f)

    def check_username(self, username_given):
        self.get_user_data()
        for user in self.user_data:
            if user["username"] == username_given:
                return True
        return False
    
    def register_user(self, input_given):
        split_details = input_given.split(",")
        username = split_details[0]
        password = split_details[1]
        password_hashed = self.password_hashing_instance.hash_password(password)
        user = {"id" : 0, "username" : " ", "password" : " "}
        id = self.get_next_available_id()
        user["id"] = id
        user["username"] = username
        user["password"] = password_hashed
        self.register(user)
    
    def register(self, details):
        self.user_data.append(details)
        with open('users.json', 'w') as f:
            json.dump(self.user_data, f, indent=4)
        
    def login(self, details):
        self.get_user_data()
        credentials_split = details.split(",")
        username = credentials_split[0]
        password = credentials_split[1]
        for user in self.user_data:
            if user["username"] == username:
                check_pass = self.password_hashing_instance.verify_password(user['password'], password)
                if check_pass == True:
                    return f"success,{user["id"]}"
                return "invalid,password"
        return "invalid,username"


    def get_existing_id(self):
        self.get_user_data()
        ids = [expense['id'] for expense in self.user_data]
        return ids

    def get_next_available_id(self):
        # Extract all the IDs from the expenses list
        ids = self.get_existing_id()
        # Sort the list of IDs
        ids.sort()
        # Check for the next available ID
        for i in range(1, len(ids)):
            if ids[0] != 1:
                return 1
            if ids[i] != ids[i-1] + 1:
                # Return the first missing ID
                return ids[i-1] + 1
        # If no gaps, return the next ID after the highest one
        return ids[-1] + 1