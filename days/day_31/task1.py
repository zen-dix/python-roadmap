def make_logger(prefix):
    def maker(text):
        print(f"{prefix} {text}")
    return maker
error_log = make_logger("[ERROR]")
error_log("Connection timeout")

