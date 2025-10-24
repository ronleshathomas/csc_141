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


user = User("Ron", "Thomas", 22, "Miami", "Ron.Thomas@yahoo.com")

# Simulate multiple login attempts
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Print the number of login attempts
print(f"Login attempts: {user.login_attempts}")

# Reset the login attempts
user.reset_login_attempts()
print(f"Login attempts after reset: {user.login_attempts}")

