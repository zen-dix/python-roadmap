class FileLogger:
    def set_file(self, filename):
        self.name = filename

    def log(self, level, message):
        log_line = f"[{level}] {message}"
        with open(self.name, "a", encoding="utf-8") as file:
            file.write(f"{log_line}\n")
        print(log_line)
backend_logger = FileLogger()
backend_logger.set_file("backend.log")
backend_logger.log("INFO", "Server started")
backend_logger.log("ERROR", "DB connection failed")