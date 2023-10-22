from users import User


class Privilege():
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


website_admin = Admin('Anton',
                      'Ruvel',
                      'a.rubel@ndsn.com',
                      '+74951001010',
                      'Moscow')

website_admin.privileges.show_privileges()
