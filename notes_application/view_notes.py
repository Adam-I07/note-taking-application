from tabulate import tabulate
import notes_application.notes_json_handling

class ViewNotes():
    def __init__(self):
        self.notes_json_handling_instance = notes_application.notes_json_handling.NotesJsonHandling()

    def view_note(self, logged_in_iser):
        self.view_notes_title()
        data = self.notes_json_handling_instance.get_display_user_notes(logged_in_iser) 
        print(tabulate(data, headers='keys', tablefmt='grid'))

    def view_notes_title(self):
        print("---------------------")
        print("All Notes:")
        print("---------------------")