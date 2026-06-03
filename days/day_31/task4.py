import itertools

def limit_yields(func):
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        limited = itertools.islice(gen, 5)

        return list(limited)

    return wrapper
@limit_yields
def infinite_counter():
    return itertools.count(1) # Бесконечный счетчик 1, 2, 3...

print(infinite_counter())