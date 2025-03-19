from fastapi import FastAPI, HTTPException
import json
from schema import schema
import auth_api

api = FastAPI()
api.include_router(auth_api.router, prefix="/auth")
# ------------------------------------------------------------------------------------------
@api.post("/notes/create")
async def create_new_note(note_data: schema.Note):
    note_dict = note_data.dict()
    existing_notes = load_data()
    existing_notes.append(note_dict)
    try:
        save_note(existing_notes)
        return "Successfully Saved"
    except:
        raise HTTPException(status_code=404, detail="Could not add note")

@api.put('/notes/edit/{note_id}')
async def edit_note(note_id: int, edited_note: schema.Note):
    existing_notes = load_data()
    for note in existing_notes:
        if note['id'] == note_id:
            note['title'] = edited_note.title
            note['content'] = edited_note.content
            note['tags'] = edited_note.tags
            note['updated_at'] = edited_note.updated_at
    try:
        save_note(existing_notes)
        return "Successfully Updated"
    except:
        raise HTTPException(status_code=404, detail="Could not update note")

@api.delete("/notes/remove/{note_id}")
async def delete_note(note_id):
    existing_notes = load_data()
    for note in existing_notes:
        if note['id'] == int(note_id):
            existing_notes.remove(note)
    try:
        save_note(existing_notes)
        return "Successfully Deleted"
    except:
        raise HTTPException(status_code=404, detail="Could not delete note")

# ------------------------------------------------------------------------------------------
# Returns the note selected by user
@api.get("/notes/specific/{note_id}")
async def get_specific_note(note_id):
    existing_notes = load_data()
    for note in existing_notes:
        if note["id"] == int(note_id):
            return note
    raise HTTPException(status_code=404, detail=f"Note with ID {note_id} not found!")

# Return all existing notes created by user logged in
@api.get("/notes/user/specific/{user_id}")
async def get_user_created_notes(user_id):
    existing_notes = load_data()
    logged_in_user_notes = []
    for note in existing_notes:
        if note["user_id"] == int(user_id):
            logged_in_user_notes.append(note)
    if logged_in_user_notes:
        return logged_in_user_notes
    raise HTTPException(status_code=404, detail="User with ID does not have notes")
    
# Returns note created dates for all notes created by user logged in
@api.get("/notes/existing/created-date/{user_id}")
async def get_user_notes_created_dates(user_id):
    existing_notes = load_data()
    existing_dates = []
    for note in existing_notes:
        if note['user_id'] == int(user_id):
            date = note['created_at'].split(" ")
            if date[0] != existing_dates:
                existing_dates.append(date[0])
    if existing_dates:
        return existing_dates
    raise HTTPException(status_code=404, detail="Did not find any dates")

# Checks the title inputted by user if it already exists returns true else returns false
@api.get("/notes/existing/check/title/{title_inputted}")
async def check_user_inputted_title_exists(title_inputted):
    existing_notes = load_data()
    for note in existing_notes:
        if note["title"].lower() == title_inputted.lower():
            return True
    return False

# Return the specific note requested
@api.get("/notes/existing/selected/note/{note_id}")
async def get_user_selected_note(note_id):
    existing_notes = load_data()
    for note in existing_notes:
        if note["id"] == int(note_id):
            return note

# Returns notes user logged in can delete
@api.get("/notes/existing/user/{user_id}")
async def get_users_selectable_notes(user_id):
    existing_notes = load_data()
    notes_selectable = []
    for note in existing_notes:
        if note['user_id'] == int(user_id):
            notes_selectable.append(note['id'])
    if notes_selectable:
        return notes_selectable
    raise HTTPException(status_code=404, detail=f"Did not find any notes that are deletable for {user_id}")

# Return all notes created on the date specified by the user logged in
@api.get("/notes/existing/day/specific/{date}/{user_id}")
async def get_user_notes_specified_day(date, user_id):
    existing_notes = load_data()
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
    existing_notes = load_data()
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
    existing_notes = load_data()
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
    existing_notes = load_data()
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
    existing_notes = load_data()
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
    ids = get_existing_id()
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

# Load all data from JSON file
def load_data():
    existing_notes = []
    try: 
        with open('../notes_application/notes.json') as f:
            existing_notes = json.load(f)
        return existing_notes
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to open and access JSON file: {str(e)}")

# Gets all exisiting id's assigned to notes and returns them
def get_existing_id():
    existing_notes = load_data()
    current_ids = [note['id'] for note in existing_notes]
    return current_ids

# Will remove the selected note by the user and triger the save_note to save the deletion
def delete_note(note_id):
    existing_notes = load_data()
    for note in existing_notes:
        if note['id'] == int(note_id):
            existing_notes.remove(note)
            save_note(existing_notes)

# Will open notes.json and save notes data from existing notes in it
def save_note(existing_notes):
    with open('../notes_application/notes.json', 'w') as f:
        json.dump(existing_notes, f, indent=4)

# ------------------------------------------------------------------------------------------