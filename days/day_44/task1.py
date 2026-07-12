class Logger:
    def log(self, message):
        return f"[LOG]: {message}"


class APIHandler:
    def __init__(self, logger: Logger):
        self.logger = logger

    def handle_request(self, endpoint):
        print(self.logger.log(f"Request to {endpoint}"))
        return "200 OK"


logger = Logger()
handler = APIHandler(logger)
print(handler.handle_request("/api/users"))
