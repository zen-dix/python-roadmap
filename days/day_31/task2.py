import time
def time_exec(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Время выполнения {func.__name__}: {end-start:.6f} сек")
        return res
    return wrapper
@time_exec
def sleep_test():
    time.sleep(1)

sleep_test()