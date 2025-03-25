from fastapi import APIRouter, HTTPException
import json
import validation.password_hashing
import schema.schema
import database_handler

router = APIRouter()
# ------------------------------------------------------------------------------------------
password_hashing_instance = validation.password_hashing.PasswordHashing()
database_handler_instance = database_handler.DatabaseHander()
# ------------------------------------------------------------------------------------------
# Regsiters new user
@router.post("/register")
async def register(details: schema.schema.UserCredentials):
    username = details.username
    password = details.password
    password_hashed = password_hashing_instance.hash_password(password)
    id = get_next_available_id()
    is_success = database_handler_instance.create_user(id, username, password_hashed)
    if is_success == "created user":
        return HTTPException(status_code=200, detail=f"Successfully Registered") 

# Returns whether the username and password entered exist or not
# If they dont which is wrong the username or password
@router.post("/check/login")
async def login(details: schema.schema.UserCredentials):
    user_data = database_handler_instance.get_all_records("users")
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
        existing_usernames = database_handler_instance.get_field_values("users", "username")
        if username_input in existing_usernames:
            return True
        raise HTTPException(status_code=404, detail=f"Unable to find username!")

# ------------------------------------------------------------------------------------------
# Returns the next available user id to use
def get_next_available_id():
    ids = database_handler_instance.get_field_values("users", "id")
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