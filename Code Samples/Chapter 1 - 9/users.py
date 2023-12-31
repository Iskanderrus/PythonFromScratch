"""

Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user.

"""


class User:

    def __init__(self, first_name, last_name, email, phone_number, city):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.city = city
        self.login_attempts = 0

    def greet_user(self):
        print(f'Hi, {self.first_name}! Nice to see you back!')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


# user_1 = User(
#     'Alex',
#     'Chasovskoy',
#     'a.n.chasovskoy@gmail.com',
#     '+79851138223',
#     'Sombor'
# )
#
# user_1.greet_user()
#
# user_1.increment_login_attempts()
# user_1.increment_login_attempts()
# user_1.increment_login_attempts()
# user_1.increment_login_attempts()
# print(f"Total {user_1.first_name}'s login attempts number is {user_1.login_attempts}")
# user_1.reset_login_attempts()
# print(f"After reset {user_1.first_name}'s login attempts number is {user_1.login_attempts}")