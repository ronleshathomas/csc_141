class User:

    def __init__(self, first_name, last_name, age, location, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"\nUser Information:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back!")


class Privileges:

    def __init__(self, privileges=None):
        if privileges is None:
            self.privileges = [
                "can add post",
                "can delete post",
                "can ban user",
                "can modify settings"
            ]
        else:
            self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges.")


class Admin(User):

    def __init__(self, first_name, last_name, age, location, email):
        super().__init__(first_name, last_name, age, location, email)
        self.privileges = Privileges()

admin_user = Admin("Namier", "Dukes", 35, "Tokyo", "Namier.Dukes@Outlook.com")

admin_user.describe_user()
admin_user.privileges.show_privileges()

