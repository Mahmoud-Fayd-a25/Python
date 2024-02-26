import datetime
import json
import re


# User class contain the registered users data
class User:
    def __init__(self, first_name, last_name, email, password, mobile_phone):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.mobile_phone = mobile_phone

    # convert user attributes to a dictionary for easy storage or processing
    def to_dict(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'password': self.password,
            'mobile_phone': self.mobile_phone
        }


# Project class contain the data of fundraising projects created by the users
class Project:
    def __init__(self, title, details, target_amount, start_date, end_date, creator, current_amount=0, backers=[], closed=False):
        self.title = title
        self.details = details
        self.target_amount = target_amount
        self.start_date = start_date
        self.end_date = end_date
        self.creator = creator  # Email address of the user who created the project
        self.current_amount = current_amount
        # List to store the emails of users who have contributed funds to the project
        self.backers = backers
        self.closed = closed  # A boolean indicating whether the project is closed

    # convert project attributes to a dictionary for easy storage or processing
    def to_dict(self):
        return {
            'title': self.title,
            'details': self.details,
            'target_amount': self.target_amount,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'creator': self.creator,
            'current_amount': self.current_amount,
            'backers': self.backers,
            'closed': self.closed
        }


# load user data from file
def load_users_from_file():
    try:
        with open('users.json', 'r') as file:
            # Check if the file is empty
            if file.readable() and file.read() == '':
                return []
            # If not empty, rewind the file and load the data
            file.seek(0)  # sets the file position to the beginning
            # reads the entire content of the file and returns a list of dictionaries, where each dictionary represents a user's data.
            users_data = json.load(file)
        users = [User(**user_data) for user_data in users_data]
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        users = []
    return users

# users a list iterates over each dictionary (user_data) in the list users_data, and for each dictionary, it creates a new User object using the **user_data syntax.
# The **user_data syntax is used for unpacking the dictionary and passing its key-value pairs as keyword arguments to the User class constructor.
# The resulting list (users) contains instances of the User class created from the JSON data.


# # load project data from file
def load_projects_from_file():
    try:
        with open('projects.json', 'r') as file:
            # Check if the file is empty
            if file.readable() and file.read() == '':
                return []
            # If not empty, rewind the file and load the data
            file.seek(0)
            projects_data = json.load(file)
        projects = [Project(**project_data) for project_data in projects_data]
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        projects = []
    return projects


# takes an object and returns a serializable version of it.
def serializer(obj):
    if isinstance(obj, User):
        return obj.__dict__
    elif isinstance(obj, Project):
        return {
            "title": obj.title,
            "details": obj.details,
            "total_money": obj.total_money,
            "start_date": obj.start_date,
            "end_date": obj.end_date,
            "creator": {
                "first_name": obj.creator.first_name,
                "last_name": obj.creator.last_name,
                "email": obj.creator.email,
                "password": "no access",
                "mobile_phone": obj.creator.mobile_phone
            }

        }
    raise TypeError("Type not serializable")


# We check if the object is an instance of the User class, and if so, we return its __dict__ attribute,
# which is a dictionary containing all the instance variables. This allows us to serialize a User instance to JSON.
# dump : convert Python objects (users list) to a JSON formatted string and write it to a file-like object.
# file : users.json
# we use a list comprehension to convert each User object to its dictionary representation (user.__dict__) and then use json.dump to write the list of dictionaries to the JSON file.
# The default=serializer parameter ensures that the custom serialization method is used for each User object encountered during the serialization process.
# indent=4 : This is an optional parameter that specifies the number of spaces to use for indentation in the resulting JSON file.
# Adding indentation makes the JSON file more human-readable


# save user data to file
def save_users_to_file(users):
    try:
        users_data = [user.__dict__ for user in users]
        with open('users.json', 'w') as file:
            json.dump(users_data, file, default=serializer, indent=4)

    except FileNotFoundError:
        return []


# save project data to file
def save_projects_to_file(projects):
    try:
        projects_data = [project.__dict__ for project in projects]
        with open('projects.json', 'w') as file:
            json.dump(projects_data, file, default=serializer, indent=4)

    except FileNotFoundError:
        return []


# check if a mobile phone number is a valid Egyptian number
def is_valid_egyptian_number(mobile_phone):
    return re.match(r'^\+20(10|11|12|15)\d{8}$', mobile_phone) is not None


# Check if the email is already registered
def is_email_registered(email, users):
    return any(user.email == email for user in users)


# user registration
def register_user():
    print("User Registration")
    users = load_users_from_file()

    while True:
        email = input("Enter your email: ")
        # ensure that the email is not registered before
        if not is_email_registered(email, users):
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")

            # password confirmation
            while True:
                password = input("Enter your password: ")
                confirm_password = input("Confirm your password: ")

                if password == confirm_password:
                    break
                else:
                    print("Passwords do not match. Please try again.")

            # ensure a valid Egyptian mobile phone number
            while True:
                mobile_phone = input(
                    "Enter your mobile phone number (+201---------): ")
                if is_valid_egyptian_number(mobile_phone):
                    break
                else:
                    print(
                        "Invalid mobile phone number. Please enter a valid Egyptian number.")

            # Continue with user registration if the email is not already registered
            user = User(first_name, last_name, email, password, mobile_phone)
            users.append(user)
            save_users_to_file(users)
            print("Registration successful!\n")
            return

        else:
            print(f"Email '{email}' is already registered.")
        choice = input(
            "Choose an option:\n1. Login\n2. Register with a new email\nEnter the option number: ")
        if choice == '1':
            login_user()
            return
        elif choice == '2':
            register_user()
            return
        else:
            print("Invalid choice. Returning to the main menu.")
            return


# user login
def login_user():
    print("User Login")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    users = load_users_from_file()

# find the first User object in the users list that matches both the provided email and hashed password.
    try:
        user = next(u for u in users if u.email.lower() == email.lower())
    except StopIteration:
        user = None

    if user.password == password:
        print(f"Welcome, {user.first_name}!\n")
        return user
    else:
        print("Invalid email or password. Please try again.\n")
        choice = input(
            "Choose an option:\n1. Login\n2. Register with a new email\nEnter the option number: ")
        if choice == '1':
            login_user()
            return None
        elif choice == '2':
            register_user()
            return None
        else:
            print("Invalid choice. Returning to the main menu.")
            return None


# Allows a logged-in user to create a new fundraising project."""
def create_project(user):
    print("Create Project")
    title = input("Enter project title: ")
    details = input("Enter project details: ")
    target_amount = float(input("Enter total targeted funds : "))
    sd = datetime.datetime.now()
    start_date = sd.strftime('%Y-%m-%d')

    while True:
        try:
            end_date_str = input("Enter end date (YYYY-MM-DD): ")
            ed = datetime.datetime.strptime(
                end_date_str, "%Y-%m-%d").date()
            end_date = ed.strftime('%Y-%m-%d')

            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    project = Project(title, details, target_amount,
                      start_date, end_date, user)
    projects = load_projects_from_file()
    projects.append(project)
    save_projects_to_file(projects)
    print("Project created successfully!\n")


# Displays information about all available projects.
def view_projects():
    print("View Projects")
    projects = load_projects_from_file()
    for project in projects:
        print(f"Title: {project.title}")
        print(f"Details: {project.details}")
        print(f"Target Amount: {project.target_amount}")
        print(f"Start Date: {project.start_date}")
        print(f"End Date: {project.end_date}")
        print(
            f"Creator: {project.creator['first_name']} {project.creator['last_name']}")
        print(f"Current Amount: {project.current_amount}")
        print("Status: Closed" if project.closed else "Status: Open")
        print("----------------------------------------------------------------")


# Allows a logged-in user to edit one of their own existing projects only.
def edit_project(user):
    print("Edit Project")
    projects = load_projects_from_file()

    # Display user's projects for selection
    user_projects = [project for project in projects if project.creator ==
                     user.email and not project.closed]

    if not user_projects:
        print("You don't have any open projects to edit.")
        return

    print("Select a project to edit:")
    for i, project in enumerate(user_projects, start=1):
        print(f"{i}. {project.title}")

    while True:
        try:
            choice = int(
                input("Enter the number corresponding to the project: "))
            if 1 <= choice <= len(user_projects):
                break
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    selected_project = user_projects[choice - 1]

    print(f"Editing project: {selected_project.title}")
    selected_project.title = input(
        "Enter new project title (press Enter to keep the current title): ") or selected_project.title
    selected_project.details = input(
        "Enter new project details (press Enter to keep the current details): ") or selected_project.details
    selected_project.target_amount = float(input(
        "Enter new total Funds targeted (press Enter to keep the current amount): ") or selected_project.target_amount)

    while True:
        try:
            new_end_date_str = input(
                "Enter new end date (YYYY-MM-DD, press Enter to keep the current date): ") or selected_project.end_date.strftime("%Y-%m-%d")
            sped = datetime.datetime.strptime(
                new_end_date_str, "%Y-%m-%d").date()
            selected_project.end_date = sped.strftime('%Y-%m-%d')
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    save_projects_to_file(projects)
    print("Project edited successfully!\n")


# Allows a logged-in user to delete one of their existing projects.
def delete_project(user):
    print("Delete Project")
    projects = load_projects_from_file()

    # Display user's projects for selection
    user_projects = [
        project for project in projects if project.creator['email'] == user.email and not project.closed]

    if not user_projects:
        print("You don't have any open projects to delete.")
        return

    print("Select a project to delete:")
    for i, project in enumerate(user_projects, start=1):
        print(f"{i}. {project.title}")

    while True:
        try:
            choice = int(
                input("Enter the number corresponding to the project: "))
            if 1 <= choice <= len(user_projects):
                break
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    selected_project = user_projects[choice - 1]

    print(f"Deleting project: ")
    projects.remove(selected_project)
    save_projects_to_file(projects)
    print(f"Project '{selected_project.title}' deleted successfully!\n")


# Allows users to search for projects by name or date.
def search_for_project():
    print("Search Projects")
    projects = load_projects_from_file()

    search_type = input("Search by (1) Name or (2) Date? Enter 1 or 2: ")

    if search_type == '1':
        search_name = input("Enter project name to search: ")
        search_results = [
            project for project in projects if search_name.lower() in project.title.lower()]
    elif search_type == '2':
        while True:
            try:
                search_date_str = input("Enter date (YYYY-MM-DD): ")
                sd = datetime.datetime.strptime(
                    search_date_str, "%Y-%m-%d").date()
                search_date = sd.strftime('%Y-%m-%d')
                break

            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
        search_results = [
            project for project in projects if search_date == project.start_date]
    else:
        print("Invalid choice. Please enter 1 or 2.")
        return

    if search_results:
        print("Search Results:")
        for project in search_results:
            print(f"Title: {project.title}")
            print(f"Details: {project.details}")
            print(f"Target Amount: {project.target_amount}")
            print(f"Start Date: {project.start_date}")
            print(f"End Date: {project.end_date}")
            print(f"Creator: {project.creator}")
            print(f"Current Amount: {project.current_amount}")
            print("Status: Closed" if project.closed else "Status: Open")
            print("===")
    else:
        print("No matching projects found.")


# Allows a logged-in user to donate to an open project.
def donate_to_project(user):
    print("Donate to Project")
    projects = load_projects_from_file()

    # Display open projects for selection
    open_projects = [project for project in projects if not project.closed]

    if not open_projects:
        print("There are no open projects to donate to.")
        return

    print("Select a project to donate to:")
    for i, project in enumerate(open_projects, start=1):
        print(f"{i}. {project.title}")

    while True:
        try:
            choice = int(
                input("Enter the number corresponding to the project: "))
            if 1 <= choice <= len(open_projects):
                break
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    selected_project = open_projects[choice - 1]

    print(f"Donating to project: {selected_project.title}")
    amount = float(input("Enter the donation amount: "))

    if amount > 0:
        selected_project.current_amount += amount
        selected_project.backers.append(user.email)
        print(f"Donation of {amount} EGP successful!\n")
    else:
        print("Invalid donation amount. Please enter a positive amount.\n")

    save_projects_to_file(projects)


def main():
    # Load existing user and project data from files
    users = load_users_from_file()
    projects = load_projects_from_file()
    logged_in_user = None

    while True:
        print("=== Crowdfunding App ===")
        if logged_in_user:
            print("1. Create Project")
            print("2. View Projects")
            print("3. Edit Project")
            print("4. Delete Project")
            print("5. Search for Projects")
            print("6. Donate to Project")
            print("7. Exit")
        else:
            print("1. Register")
            print("2. Login")
            print("3. Exit")

        choice = input("Enter your choice: ")

        if not logged_in_user:
            if choice == '1':
                register_user()
            elif choice == '2':
                logged_in_user = login_user()
            elif choice == '3':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")
        else:
            if choice == '1':
                create_project(logged_in_user)
            elif choice == '2':
                view_projects()
            elif choice == '3':
                edit_project(logged_in_user)
            elif choice == '4':
                delete_project(logged_in_user)
            elif choice == '5':
                search_for_project()
            elif choice == '6':
                donate_to_project(logged_in_user)
            elif choice == '7':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
