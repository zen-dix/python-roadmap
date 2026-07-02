class UserRegistryService:
    def __init__(self):
        self.__registered_user = {}

    def register_account(self, username, password):
        if username in self.__registered_user:
            raise UserConflictError(
                f"Registration failed: User {username} already exists."
            )
        else:
            self.__registered_user[username] = password

    def verify_credentials(self, username, password):
        if (
            username in self.__registered_user
            and self.__registered_user.get(username) == password
        ):
            return f"session_token_{username}"
        else:
            return None


class UserConflictError(Exception):
    pass


backend_auth = UserRegistryService()
backend_auth.register_account("gleb", "secure_password")

try:
    backend_auth.register_account("gleb", "different_password")
except UserConflictError as error:
    print(error)

active_session = backend_auth.verify_credentials("gleb", "secure_password")
print(f"Session state: {active_session}")
