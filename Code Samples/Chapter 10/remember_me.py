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


def get_new_userdata(path_object: Path) -> str:
    """
    Function to get username of a new user and save it in the json file.
    :param path_object: Path object to save the username in json file.
    :return: Username as a string.
    """
    username = input('What is your name? ').strip().lower()
    user_email = input('What is your email? ').strip().lower()
    user_city = input('What is your city? ').strip().lower()
    user_birth_year = int(input('What is your birth year? '))
    user_data = {
        'username': username,
        'email': user_email,
        'city': user_city,
        'year': user_birth_year,
    }
    contents = json.dumps(user_data)
    path_object.write_text(contents)
    return username


def greet_user() -> None:
    """
    Function to greet user if username was saved in the json file. Or store the username in json file if it is new.
    :return: None
    """

    path = Path('username.json')
    user_data = get_stored_userdata(path)
    if user_data:
        print(f"Hi, {user_data['username'].title()}! Nice to see you again!")
        print(f"Your were born in {user_data['year']} and "
              f"you live now in {user_data['city'].title()}, your email is {user_data['email']}.")

    else:
        username = get_new_userdata(path)

        print(f"We'll remember you when you come back, {username}!")

greet_user()
