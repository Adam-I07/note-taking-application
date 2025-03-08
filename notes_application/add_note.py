import notes_application.notes_validation
from datetime import datetime
import notes_application.notes_json_handling

class AddNote():
    def __init__(self):
        self.notes_validation_instance = notes_application.notes_validation.NotesValidation()
        self.notes_json_handling_instance = notes_application.notes_json_handling.NotesJsonHandling()

    def add_new_note(self, user_id):
        note = {"id" : "", "user_id" : "", "title" : "", "content" : "", "tags" : "", "created_at" : "", "updated_at": ""}
        note["id"] = self.notes_validation_instance.get_next_id()
        note["user_id"] = user_id
        self.add_note_title()
        title = self.notes_validation_instance.title_validation()
        note["title"] = title
        content = self.notes_validation_instance.content_validation()
        note["content"] = content
        tags = self.notes_validation_instance.tags_validation()
        note["tags"] = tags
        date_format = '%d/%m/%Y %H:%M:%S'
        current_date_time = datetime.now().strftime(date_format)
        note["created_at"] = current_date_time
        note["updated_at"] = current_date_time
        confirmation = self.notes_validation_instance.confirm_save()
        if confirmation == True:
            # self.notes_json_handling_instance.add_new_note(note)
            print(note)
            self.notes_json_handling_instance.add_new_note(note) 
        else:
            return


    def add_note_title(self):
        print("---------------------")
        print("Add Note")
        print("---------------------")