def retry(attempts=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(attempts):
                try:
                    result = func(*args, **kwargs)
                    print("Connected to the database successfully!")
                    break
                except ConnectionError:
                    print(f"Attempt {i + 1} failed. Retrying...")
            else:
                raise ConnectionError()
            return result

        return wrapper

    return decorator


class DatabaseConnector:
    def __init__(self):
        self._attempts = 0

    @retry(attempts=3)
    def connect(self):
        self._attempts += 1
        if self._attempts < 3:
            raise ConnectionError()


database = DatabaseConnector()
database.connect()
