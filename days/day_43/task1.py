class UserProfile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def password(self):
        return len(self._password) * "*"

    @password.setter
    def password(self, new_password: str):
        if len(new_password) < 8:
            raise ValueError("Password is too short")
        self._password = new_password


user = UserProfile("zendix", "super_secret_password")
print(user.password)
user.password = "new_pass_123"
print(user.password)
try:
    user.password = "123"
except ValueError:
    print("Password is too short")
