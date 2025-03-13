import notes_application.notes_json_handling
import notes_application.notes_validation
from colorama import Fore

class FilterNotesBackend():
    def __init__(self):
        self.notes_json_handling_instance = notes_application.notes_json_handling.NotesJsonHandling()
        self.notes_validation_instance = notes_application.notes_validation.NotesValidation()

    def filter_by_tags(self, logged_in_user):
        tag_selected = self.select_tag()
        data = self.notes_json_handling_instance.filter_by_tag(tag_selected, logged_in_user)
        if data:
            self.notes_validation_instance.create_table(data)
        else:
            print(Fore.RED + "No note with the tag selected exist!" + Fore.WHITE)

    def select_tag(self):
        tag_options = ["work", "personal", "school", "shopping", "travel", "health", "finance", "ideas", "recipes", "urgent", "important", "todo", "done", "in-progress"]
        print("---------------------")
        num = 0
        print("Tags:")
        for tag in tag_options:
            num = num + 1
            print(f"{num}. {tag}")
        print("---------------------")
        while True:
            user_input = input("Enter numerical value assosciated with the tag you would like to select: ")
            check = self.notes_validation_instance.check_user_input_type(user_input)
            if check == 'int':
                if int(user_input) > 0 and int(user_input) <= len(tag_options):
                    return tag_options[int(user_input)-1]
                else:
                    print(Fore.RED + "Invalid tag selected! Only enter a valid numerical value assosicated with a tag!" + Fore.WHITE)
            else:
                print(Fore.RED + "Invalid input enter a valid numerical input!" + Fore.WHITE)

    def filter_by_content_title(self, logged_in_user):
        filter_choice = self.select_title_content()
        while True:
            user_input = input("Enter the phrase or word you want to filter by: ")
            if user_input:
                data = self.notes_json_handling_instance.filter_by_phrase(user_input, filter_choice, logged_in_user)
                if data:
                    self.notes_validation_instance.create_table(data)
                    return
                else:
                    print(Fore.RED + f"No content containing {user_input} could be found!" + Fore.WHITE)
            else:
                print(Fore.RED + "You must enter an input phrase or work!" + Fore.WHITE)

    def select_title_content(self):
        print("Select what you would like to filter")
        print("1. Title")
        print("2. Content")
        while True:
            user_choice = input("Enter the numerical value assosciated with option you would like to filter by: ")
            if user_choice == '1':
                return "title"
            elif user_choice == '2':
                return "content"
            else:
                print(Fore.RED + "You have entered an invalid input! Try again!" + Fore.WHITE)

    def select_year(self, logged_in_user):
        dates = self.notes_json_handling_instance.return_dates(logged_in_user)
        years = self.convet_date_to_year(dates)
        self.print_dates(years)
        while True:
            user_input = input("Enter numerical value assosciated with the year you would like to select: ")
            print("---------------------")
            check = self.notes_validation_instance.check_user_input_type(user_input)
            if check == 'int':
                if int(user_input) > 0 and int(user_input) <= len(years):
                    data = self.notes_json_handling_instance.get_specific_notes_by_years(years[int(user_input)-1], logged_in_user)
                    self.notes_validation_instance.create_table(data)
                    return
                else:
                    print(Fore.RED + "Invalid year entered! Only enter a valid numerical value assosicated with a year!")
            else:
                print(Fore.RED + "Invalid input enter a valid numerical input!" + Fore.WHITE)


    def convet_date_to_year(self, dates):
        years = []
        for date in dates:
            split_date = date.split("/")
            year = split_date[2]
            if year not in years:
                years.append(year)
        return years

    def select_month(self, logged_in_user):
        dates = self.notes_json_handling_instance.return_dates(logged_in_user)
        months = self.convert_date_to_month(dates)
        self.print_dates(months)
        while True:
            user_input = input("Enter numerical value assosciated with the month you would like to select: ")
            print("---------------------")
            check = self.notes_validation_instance.check_user_input_type(user_input)
            if check == 'int':
                if int(user_input) > 0 and int(user_input) <= len(months):
                    data = self.notes_json_handling_instance.get_specific_notes_by_month(months[int(user_input)-1], logged_in_user)
                    self.notes_validation_instance.create_table(data)
                    return
                else:
                    print(Fore.RED + "Invalid month entered! Only enter a valid numerical value assosicated with a month!" + Fore.WHITE)
            else:
                print(Fore.RED + "Invalid input enter a valid numerical input!" + Fore.WHITE)

    def convert_date_to_month(self, dates):
        months = []
        for date in dates:
            split_date = date.split("/")
            month = f"{split_date[1]}/{split_date[2]}"
            if month not in months:
                months.append(month)
        return months

    def select_day(self, logged_in_user):
        dates = self.notes_json_handling_instance.return_dates(logged_in_user)
        self.print_dates(dates)
        while True:
            user_input = input("Enter numerical value assosciated with the date you would like to select: ")
            print("---------------------")
            check = self.notes_validation_instance.check_user_input_type(user_input)
            if check == 'int':
                if int(user_input) > 0 and int(user_input) <= len(dates):
                    data = self.notes_json_handling_instance.get_specific_notes_by_date(dates[int(user_input)-1], logged_in_user)
                    self.notes_validation_instance.create_table(data)
                    return
                else:
                    print(Fore.RED + "Invalid date entered! Only enter a valid numerical value assosicated with a date!" + Fore.WHITE)
            else:
                print(Fore.RED + "Invalid input enter a valid numerical input!" + Fore.WHITE)

    def print_dates(self, dates):
        num = 0
        print("---------------------")
        for date in dates:
            num += 1
            print(f"{num}. {date}")
        print("---------------------")

    