class Authenticator:
    def verify(self, token):
        if token == "secret_key":
            return True
        else:
            return False


class Route:
    def __init__(self, path: str, authenticator: Authenticator):
        self.path = path
        self.auth = authenticator

    def access(self, token):
        if self.auth.verify(token):
            return f"Access granted to {self.path}"
        else:
            return "403 Forbidden"


auth = Authenticator()
route = Route("/dashboard", auth)
print(route.access("wrong_key"))
print(route.access("secret_key"))
