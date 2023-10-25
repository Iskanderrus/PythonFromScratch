from pathlib import Path
import json


def get_stored_username(path_object: Path) -> str or None:
    """
    Function to extract previously saved username.
    :param path_object: Path object for file containing username.
    :return: Username as a string value or None object if path object doesn't exist.
    """

    if path_object.exists():
        path_contents = path_object.read_text()
        stored_name = json.loads(path_contents)
        return stored_name
    else:
        return None


def get_new_username(path_object: Path) -> str:
    """
    Function to get username of a new user and save it in the json file.
    :param path_object: Path object to save the username in json file.
    :return: Username as a string.
    """
    username = input('What is your name? ')
    contents = json.dumps(username)
    path_object.write_text(contents)
    return username


def greet_user() -> None:
    """
    Function to greet user if username was saved in the json file. Or store the username in json file if it is new.
    :return: None
    """

    path = Path('username.json')
    user_name = get_stored_username(path)
    if user_name:
        print(f"Hi, {user_name}! Nice to see you again!")

    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")


greet_user()
