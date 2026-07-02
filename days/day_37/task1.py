class DBConfig:
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password


user = DBConfig("127.0.0.1", 5432, "admin", "qwerty")
print(f"Connection to {user.host}:{user.port} as {user.username}")

