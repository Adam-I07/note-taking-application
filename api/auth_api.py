from fastapi import APIRouter, HTTPException
import json
import validation.password_hashing
import schema.schema

router = APIRouter()
# ------------------------------------------------------------------------------------------
password_hashing_instance = validation.password_hashing.PasswordHashing()
# ------------------------------------------------------------------------------------------
# Regsiters new user
@router.post("/register")
async def register(details: schema.schema.UserCredentials):
    username = details.username
    password = details.password
    password_hashed = password_hashing_instance.hash_password(password)
    user = {"id" : 0, "username" : " ", "password" : " "}
    id = get_next_available_id()
    user["id"] = id
    user["username"] = username
    user["password"] = password_hashed
    is_success = register(user)
    if is_success == "success":
        return HTTPException(status_code=200, detail=f"Successfully Registered") 

# Returns whether the username and password entered exist or not
# If they dont which is wrong the username or password
@router.post("/check/login")
async def login(details: schema.schema.UserCredentials):
    user_data = load_user_data()
    username = details.username
    password = details.password
    for user in user_data:
        if user["username"] == username:
            check_pass = password_hashing_instance.verify_password(user['password'], password)
            if check_pass == True:
                return HTTPException(status_code=200, detail=f"Success, {user['id']}")
            raise HTTPException(status_code=401, detail=f"Invalid password")
    raise HTTPException(status_code=401, detail=f"Invalid username")

# Returns if the username inputted already exists or not
@router.get("/check/username/{username_input}")
async def check_username(username_input):
        user_data = load_user_data()
        for user in user_data:
            if user["username"] == username_input:
                return True
        raise HTTPException(status_code=404, detail=f"Unable to find username!")

# ------------------------------------------------------------------------------------------

# Open users.json file and load all data
def load_user_data():
    user_data = []
    try: 
        with open('../user_handling/users.json') as f:
            user_data = json.load(f)
        return user_data
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to open and access JSON file: {str(e)}")

# Adds new user to user_data dictionaty opens json file and saves all information from dictionary in it
def register(details):
    user_data = load_user_data()
    user_data.append(details)
    try:
        with open('../user_handling/users.json', 'w') as f:
            json.dump(user_data, f, indent=4)
        return "success"
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to open and access JSON file: {str(e)}")

# Gets all exisiting id's assigned to notes and returns them
def get_existing_id():
    user_data = load_user_data()
    ids = [expense['id'] for expense in user_data]
    return ids

# Returns the next available user id to use
def get_next_available_id():
    ids = get_existing_id()
    ids.sort()
    for i in range(1, len(ids)):
        if ids[0] != 1:
            return 1
        if ids[1] != 2:
            return 2
        if ids[i] != ids[i-1] + 1:
            return ids[i-1] + 1
    return ids[-1] + 1
# ------------------------------------------------------------------------------------------