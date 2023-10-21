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


class Privilege:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f'List of available privileges: ')
        for privilege in self.privileges:
            print(f"\t\t- {privilege}")


class Admin(User):
    def __init__(self, first_name, last_name, email, phone_number, city):
        super().__init__(first_name, last_name, email, phone_number, city)
        self.privileges = Privilege()
