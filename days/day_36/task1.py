class Process:
    def __init__(self, name, pid):
        self.name = name
        self.pid = pid


class PortScanner:
    def scan(self, target_ip, port):
        print(f"[+] Scanning {target_ip}:{port}...")


class APIRouter:
    def setup(self):
        self.routes = []

    def add_route(self, path):
        self.routes.append(path)

    def show_routes(self):
        print(f"Active routes: {', '.join(self.routes)}")


class FileLogger:
    def set_file(self, filename):
        self.name = filename

    def log(self, level, message):
        log_line = f"[{level}] {message}"
        with open(self.name, "a", encoding="utf-8") as file:
            file.write(f"{log_line}\n")
        print(log_line)


proc_nginx = Process("nginx", 1024)
proc_postgres = Process("postgres", 2048)
print(f"Процесс [{proc_nginx.name}] запущес с PID [{proc_nginx.pid}].")
print(f"Процесс [{proc_postgres.name}] запущес с PID [{proc_postgres.pid}].")

scanner = PortScanner()
scanner.scan("113.3.4.1", 80)
scanner.scan("342.4.43.2", 443)
router = APIRouter()
router.setup()
router.add_route("/users")
router.add_route("/post")
router.show_routes()

backend_logger = FileLogger()
backend_logger.set_file("backend.log")
backend_logger.log("INFO", "Server started")
backend_logger.log("ERROR", "DB connection failed")
