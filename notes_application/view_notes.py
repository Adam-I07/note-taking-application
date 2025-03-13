import notes_application.notes_validation
import notes_application.notes_json_handling

class ViewNotes():
    def __init__(self):
        self.notes_json_handling_instance = notes_application.notes_json_handling.NotesJsonHandling()
        self.notes_validation_instance = notes_application.notes_validation.NotesValidation()

    def view_note(self, logged_in_user):
        self.view_notes_title()
        data = self.notes_json_handling_instance.get_display_user_notes(logged_in_user) 
        self.notes_validation_instance.create_table(data)

    def view_notes_title(self):
        print("---------------------")
        print("All Notes:")
        print("---------------------")