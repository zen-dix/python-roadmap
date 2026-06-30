import time


def delay_execution(seconds):
    def dec(func):
        def wrapped(*args, **kwargs):
            time.sleep(seconds)
            return func(*args, **kwargs)

        return wrapped

    return dec


@delay_execution(1)
def fetch_data():
    return "Data fetched!"


print(fetch_data())
