class DatabaseManager:
    def __init__(self, host: str, port: int):
        self._host = host
        self._port = port
        self._is_connected = False

    @staticmethod
    def validate_port(port: int):
        if not isinstance(port, int) or not (1 <= port <= 65535):
            raise ValueError(
                f"Invalid port: {port}. Must be an int between 1 and 65535."
            )

    @classmethod
    def from_uri(cls, uri: str):
        host, port = uri.replace("db://", "").split(":")
        port = int(port)
        cls.validate_port(port)
        return cls(host, port)

    @property
    def url(self):
        return f"db://{self._host}:{self._port}"

    @property
    def status(self):
        return "Online" if self._is_connected else "Offline"

    def connect(self):
        self._is_connected = True
        print(f"Connected to {self.url}")


# Проверка
db = DatabaseManager.from_uri("db://192.168.0.10:27017")
print(f"URL: {db.url}")
print(f"Status: {db.status}")
db.connect()
print(f"Status: {db.status}")
