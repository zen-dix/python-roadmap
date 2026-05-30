def log_message(msg):
    with open("system.log", "a", encoding="utf-8") as file:
        file.write(msg)
log_message("feature/file-log")