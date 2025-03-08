from tabulate import tabulate
import notes_application.notes_json_handling

class ViewNotes():
    def __init__(self):
        self.notes_json_handling_instance = notes_application.notes_json_handling.NotesJsonHandling()

    def view_note(self):
        self.view_notes_title()
        self.notes_json_handling_instance.get_data()
        data = self.notes_json_handling_instance.existing_notes
        print(tabulate(data, headers='keys', tablefmt='grid'))

    def view_notes_title(self):
        print("---------------------")
        print("All Notes:")
        print("---------------------")