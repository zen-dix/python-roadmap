import itertools
import pathlib


class DBConfig:
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password


class UserSession:
    def __init__(self, user_id, token):
        self.user_id = user_id
        self.token = token
        self.is_active = True


class LinuxProcess:
    def __init__(self, pid, name):
        self.pid = pid
        self.name = name
        self.status = "running"

    def kill(self):
        self.status = "terminated"
        print(f"Process {self.name} (PID: {self.pid}) killed")


class APIRouter:
    def __init__(self, base_url):
        self.base_url = base_url

    def build_url(self, endpoint):
        return f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"


class LoadBalancer:
    def __init__(self, ip):
        self.server_pool = itertools.cycle(ip)

    def get_next_server(self):
        return next(self.server_pool)


class AppLogger:
    def __init__(self, name):
        self.file_path = pathlib.Path(name)

    def log(self, message):
        try:
            with open(self.file_path, "a", encoding="utf-8") as file:
                file.write(message)
        except PermissionError:
            print("You haven't permissons")
        except OSError:
            print("You have problems with os")


user = DBConfig("127.0.0.1", 5432, "admin", "qwerty")
print(f"Connection to {user.host}:{user.port} as {user.username}")

obj = UserSession(101, "abc-123")
print(obj.is_active)

process = LinuxProcess(4096, "nginx")
process.kill()

api = APIRouter("https://api.github.com")
print(api.build_url("/users/zendix"))

servers = LoadBalancer(["192.168.1.1", "192.168.1.2", "192.168.1.3"])
for i in range(5):
    print(servers.get_next_server())
