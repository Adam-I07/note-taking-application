import json

class NotesJsonHandling():
    def __init__(self):
        self.existing_notes = []

    def get_data(self):
        try: 
            self.existing_notes.clear()
        except:
            pass
        with open('notes_application/notes.json') as f:
                self.existing_notes = json.load(f)
    
    def get_display_user_notes(self, user_id):
        self.get_data()
        logged_in_user_notes = []
        for note in self.existing_notes:
            if note["user_id"] is int(user_id):
                logged_in_user_notes.append(note)
        return logged_in_user_notes
    
    def check_title(self, input):
        self.get_data()
        for note in self.existing_notes:
            if note["title"] == input:
                return True
        return False
    
    def add_new_note(self, to_add):
        self.get_data()
        self.existing_notes.append(to_add)
        with open('notes_application/notes.json', 'w') as f:
            json.dump(self.existing_notes, f, indent=4)

    def edit_note(self, edit_note):
        self.get_data()
        for note in self.existing_notes:
            if note['id'] == edit_note['id']:
                note['title'] = edit_note['title']
                note['content'] = edit_note['content']
                note['tags'] = edit_note['tags']
                note['updated_at'] = edit_note ['updated_at']
        self.save_note()
    
    def filter_by_tag(self, tag_selected, logged_in_user):
        self.get_data()
        data = []
        for note in self.existing_notes:
            if tag_selected in note['tags'] and note['user_id'] is int(logged_in_user):
                data.append(note)
        return data

    def filter_by_phrase(self, word, filter_choice, logged_in_user):
        self.get_data()
        notes = []
        for note in self.existing_notes:
            if word in note[filter_choice] and note['user_id'] is int(logged_in_user):
                notes.append(note)
        return notes

    def get_user_specific_notes_id(self, user_id):
        self.get_data()
        notes_can_be_deleted = []
        for note in self.existing_notes:
            if note['user_id'] == int(user_id):
                notes_can_be_deleted.append(note['id'])
        return notes_can_be_deleted
    
    def get_specific_note(self, note_id):
        self.get_data()
        for note in self.existing_notes:
            if note["id"] == note_id:
                return note
            
    def get_specific_notes_by_years(self, date, logged_in_user):
        self.get_data()
        notes = []
        for note in self.existing_notes:
            dates = note['created_at'].split(" ")
            split_date = dates[0].split("/")
            if split_date[2] in date and note['user_id'] is int(logged_in_user):
                notes.append(note)
        return notes
        
    def get_specific_notes_by_month(self, date, logged_in_user):
        self.get_data()
        notes = []
        for note in self.existing_notes:
            dates = note['created_at'].split(" ")
            split_date = dates[0].split("/")
            month = f"{split_date[1]}/{split_date[2]}"
            if month in date and note['user_id'] is int(logged_in_user):
                notes.append(note)
        return notes
    
    def get_specific_notes_by_date(self, date, logged_in_user):
        self.get_data()
        notes = []
        for note in self.existing_notes:
            dates = note['created_at'].split(" ")
            if dates[0] == date and note['user_id'] is int(logged_in_user):
                notes.append(note)
        return notes
    
    def return_dates(self, logged_user):
        self.get_data()
        dates = []
        for note in self.existing_notes:
            if note['user_id'] == int(logged_user):
                date = note['created_at'].split(" ")
                if date[0] != dates:
                    dates.append(date[0])
        return dates

    def delete_note(self, note_id):
        self.get_data()
        for note in self.existing_notes:
            if note['id'] == int(note_id):
                self.existing_notes.remove(note)
                self.save_note()
    
    def save_note(self):
        with open('notes_application/notes.json', 'w') as f:
            json.dump(self.existing_notes, f, indent=4)

    def get_next_id(self):
        # Extract all the IDs from the expenses list
        ids = self.get_existing_id()
        # Sort the list of IDs
        ids.sort()
        # Check for the next available ID
        if ids == []:
            return 1
        else:
            for i in range(1, len(ids)):
                if ids[0] != 1:
                    return 1
                if ids[1] != 2:
                    return 2
                if ids[i] != ids[i-1] + 1:
                    # Return the first missing ID
                    return ids[i-1] + 1
        # If no gaps, return the next ID after the highest one
        return ids[-1] + 1
    
    def get_existing_id(self):
        self.get_data()
        current_ids = [note['id'] for note in self.existing_notes]
        return current_ids


