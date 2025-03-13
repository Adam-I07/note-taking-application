import notes_application.view_notes
import notes_application.notes_validation

class DeleteNote():
    def __init__(self):
        self.view_notes_instance = notes_application.view_notes.ViewNotes()
        self.notes_validation_instance = notes_application.notes_validation.NotesValidation()

    def delete_note(self, user_logged_in):
        self.view_notes_instance.view_note(user_logged_in)
        delete = self.notes_validation_instance.select_note_to_delete(user_logged_in)
        if delete == 'back':
            return
        