class AppLogger:
    def __init__(self, name):
        self.file_path = pathlib.Path(name)

    def log(self, message):
        try:
            with open(self.file_path, "a", encoding="utf-8") as file:
                file.write(message+"\n")
        except PermissionError:
            print("You haven't permissons")
        except OSError:
            print("You have problems with os")

app = AppLogger("log.txt")
app.log("first log")
app.log("first log")
