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

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):

    def __init__(self, first_name, last_name, age, location, email):
        super().__init__(first_name, last_name, age, location, email)
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user",
            "can modify settings"
        ]

    def show_privileges(self):
        print(f"\nAdmin Privileges for {self.first_name} {self.last_name}:")
        for privilege in self.privileges:
            print(f"- {privilege}")


admin_user = Admin("Ray", "Edwards", 35, "Delware", "Ray.Ed@example.com")

admin_user.describe_user()
admin_user.show_privileges()

