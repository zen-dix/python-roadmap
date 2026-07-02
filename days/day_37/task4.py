class APIRouter:
    def __init__(self, base_url):
        self.base_url = base_url

    def build_url(self, endpoint):
        return f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
api = APIRouter("https://api.github.com")
print(api.build_url("/users/zendix"))