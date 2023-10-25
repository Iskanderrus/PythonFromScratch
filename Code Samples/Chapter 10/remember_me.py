from pathlib import Path
import json


def get_stored_userdata(path_object: Path) -> dict or None:
    """
    Function to extract previously saved userdata.
    :param path_object: Path object for file containing username.
    :return: Userdata as a dictionary or None object if path object doesn't exist.
    """

    if path_object.exists():
        path_contents = path_object.read_text()
        stored_data = json.loads(path_contents)
        return stored_data
    else:
        return None


def get_new_userdata(path_object: Path) -> None:
    """
    Function to get username of a new user and save it in the json file.
    :param path_object: Path object to save the username in json file.
    :return: Username as a string.
    """
    user_data = {
        'username': input('What is your name? ').strip().lower(),
        'email': input('What is your email? ').strip().lower(),
        'city': input('What is your city? ').strip().lower(),
        'year': int(input('What is your birth year? ')),
    }
    contents = json.dumps(user_data)
    path_object.write_text(contents)
    print(f"We'll remember you when you come back, {user_data['username'].title()}!")


def greet_user() -> None:
    """
    Function to greet user if username was saved in the json file. Or store the username in json file if it is new.
    :return: None
    """

    path = Path('userdata.json')
    user_data = get_stored_userdata(path)
    try:
        user_name_check = input(f"Is you username {user_data['username'].title()}? y/n\n").lower().strip()
    except TypeError:
        get_new_userdata(path)

    else:
        if user_name_check == 'n':
            get_new_userdata(path)

        elif user_name_check == 'y':
            print(f"Hi, {user_data['username'].title()}! Nice to see you again!")
            print(f"Your were born in {user_data['year']} and "
                  f"you live now in {user_data['city'].title()}, "
                  f"your email is {user_data['email']}.")

        else:
            print('Not valid input. Try again.')
            greet_user()


greet_user()
