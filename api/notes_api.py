from fastapi import FastAPI, HTTPException
import json
from schema import schema
import auth_api
import database_handler

api = FastAPI()
api.include_router(auth_api.router, prefix="/auth")

database_handler_instance = database_handler.DatabaseHander()
# ------------------------------------------------------------------------------------------
@api.post("/notes/create")
async def create_new_note(note_data: schema.Note):
    try:
        response = database_handler_instance.create_note(note_data)
        return response
    except Exception as e:
        raise HTTPException(status_code=404, detail="Could not add note")

@api.put('/notes/edit')
async def edit_note(edited_note: schema.Note):
    try:
        response = database_handler_instance.edit_note(edited_note)
        return response
    except:
        raise HTTPException(status_code=404, detail="Could not update note")

@api.delete("/notes/remove/{note_id}")
async def delete_note(note_id):
    try:
        response = database_handler_instance.delete_record("notes", {note_id})
        if response == "Successfully deleted record":
            return "Successfully Deleted"
        else:
            raise "No record found with ID in table"
    except:
        raise HTTPException(status_code=404, detail="Could not delete note")

# ------------------------------------------------------------------------------------------
# Return all existing notes created by user logged in
@api.get("/notes/user/specific/{user_id}")
async def get_user_created_notes(user_id):
    user_notes = database_handler_instance.select_by_id("notes", int(user_id))
    if user_notes:
        return user_notes
    raise HTTPException(status_code=404, detail="User with ID does not have notes")
    
# Returns note created dates for all notes created by user logged in
@api.get("/notes/existing/created-date/{user_id}")
async def get_user_notes_created_dates(user_id):
    dates = database_handler_instance.get_field_values("notes", "created_at", int(user_id))
    existing_dates = []
    for note in dates:
        date_split = note.split(" ")
        if date_split[0] not in existing_dates:
            existing_dates.append(date_split[0])
    if existing_dates:
        return existing_dates
    raise HTTPException(status_code=404, detail="Did not find any dates")

# Checks the title inputted by user if it already exists returns true else returns false
@api.get("/notes/existing/check/title/{title_inputted}")
async def check_user_inputted_title_exists(title_inputted):
    existing_titles = database_handler_instance.get_specific_field_value("notes", "title")
    for title in existing_titles:
        if title.lower() == title_inputted.lower():
            return True
    return False

# Return the specific note requested
@api.get("/notes/existing/selected/note/{note_id}")
async def get_user_selected_note(note_id):
    note = database_handler_instance.get_specific_note("notes", int(note_id))
    return note

# Returns notes of user logged in
@api.get("/notes/existing/user/{user_id}")
async def get_users_selectable_notes(user_id):
    user_notes = database_handler_instance.get_field_values_according_userid("notes", "id", int(user_id))
    if user_notes:
        return user_notes
    raise HTTPException(status_code=404, detail=f"Did not find any notes that are deletable for {user_id}")

# Return all notes created on the date specified by the user logged in
@api.get("/notes/existing/day/specific/{date}/{user_id}")
async def get_user_notes_specified_day(date, user_id):
    existing_notes = database_handler_instance.select_by_id("notes", int(user_id))
    notes = []
    for note in existing_notes:
        dates = note['created_at'].split(" ")
        if dates[0] == date and note['user_id'] is int(user_id):
            notes.append(note)
    if notes:
        return notes
    raise HTTPException(status_code=404, detail="Did not find any notes on selected date for user")

# Returns all notes created on the month specified by the user logged in
@api.get("/notes/existing/month/specific/{date}/{user_id}")
async def get_user_notes_specified_month(date, user_id):
    existing_notes = database_handler_instance.select_by_id("notes", int(user_id))
    notes = []
    for note in existing_notes:
        dates = note['created_at'].split(" ")
        split_date = dates[0].split("-")
        month = f"{split_date[1]}-{split_date[2]}"
        if month in date and note['user_id'] is int(user_id):
            notes.append(note)
    if notes:
        return notes
    raise HTTPException(status_code=404, detail="Did not find any notes on month selected for user")

# Returns all notes created on the year specified by the user logged in
@api.get("/notes/existing/year/specific/{year}/{user_id}")
async def get_user_notes_specified_year(year, user_id):
    existing_notes = database_handler_instance.select_by_id("notes", int(user_id))
    notes = []
    for note in existing_notes:
        dates = note['created_at'].split(" ")
        split_date = dates[0].split("-")
        if split_date[2] in year and note['user_id'] is int(user_id):
            notes.append(note)
    if notes:
        return notes
    raise HTTPException(status_code=404, detail=f"Did not find any notes in year for user")

# Return all notes that contain the phrase/word inputted by the user
@api.get("/notes/existing/phrase/specific/{word}/{filter_choice}/{user_id}")
async def get_user_word_specific_filter_notes(word, filter_choice, user_id):
    existing_notes = database_handler_instance.select_by_id("notes", int(user_id))
    notes = []
    for note in existing_notes:
        if word.lower() in note[filter_choice].lower() and note['user_id'] is int(user_id):
            notes.append(note)
    if notes: 
        return notes
    raise HTTPException(status_code=404, detail="Did not find any notes containing the word/phrase entered")

# Return all notes containing the tag selected by the user
@api.get("/notes/existing/tag/specific/{tag_selected}/{user_id}")
async def get_user_tag_specific_filter_notes(tag_selected: str, user_id: int):
    existing_notes = database_handler_instance.select_by_id("notes", int(user_id))
    data = []
    for note in existing_notes:
        if tag_selected in note['tags'] and note['user_id'] is int(user_id):
            data.append(note)
    if data:
        return data
    raise HTTPException(status_code=404, detail="Did not find any notes with the selected tag")


# Returns the next available note id to use
@api.get("/notes/next/available/id")
async def get_next_id():
    ids = database_handler_instance.get_specific_field_value("notes", "id")
    ids.sort()
    if ids == []:
        return 1
    else:
        for i in range(1, len(ids)):
            if ids[0] != 1:
                return 1
            if ids[1] != 2:
                return 2
            if ids[i] != ids[i-1] + 1:
                return ids[i-1] + 1
    return ids[-1] + 1

# ------------------------------------------------------------------------------------------