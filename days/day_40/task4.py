class BaseEndpoint:
    def __init__(self, path):
        self.path = path

    def get(self):
        raise NotImplementedError("Method not allowed")

    def post(self):
        raise NotImplementedError("Method not allowed")

    def handle_request(self, method):
        if method == "GET":
            return self.get()
        elif method == "POST":
            return self.post()


class LoginEndpoint(BaseEndpoint):
    def post(self):
        return f"Processing login at {self.path}"


class ProfileEndpoint(BaseEndpoint):
    def get(self):
        return f"Fetching profile at {self.path}"


login = LoginEndpoint("/api/v1/login")
print(login.handle_request("POST"))
profile = ProfileEndpoint("/api/v1/profile")
try:
    print(profile.handle_request("POST"))
except NotImplementedError:
    print("Error: thish method is not suuported for this path")
