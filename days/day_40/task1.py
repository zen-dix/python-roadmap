class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_headers(self):
        return {"Content-Type": "application/json"}


class GitHubClient(APIClient):
    def __init__(self, base_url, token):
        super().__init__(base_url)
        self.token = token

    def get_headers(self):
        self.header_dict = super().get_headers()
        self.header_dict["Authorization"] = f"Bearer {self.token}"
        return self.header_dict


client = GitHubClient("https://api.github.com", "ghp_12345")
print(client.get_headers())
