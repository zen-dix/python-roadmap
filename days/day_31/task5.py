def simple_cache(func):
    cache = {}
    last_args = tuple()
    def wrapper(*args, **kwargs):
        nonlocal last_args
        if args != last_args:
            for data in args:
                cache[data] = func(data)
            last_args = args
        return  tuple(cache[data] for data in args)
    return wrapper
@simple_cache
def heavy_math(x):
    print(f"Вычисляю для {x}...")
    return x ** 2

print(*heavy_math(10))
print(*heavy_math(10)) # Во второй раз строка "Вычисляю..." не должна напечататься