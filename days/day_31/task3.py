def require_ints(func):
    def checker(*args, **kwargs):
        if list(num for num in args if not isinstance(num, int)):
            return f"Ошибка: ожидаются только целые числа"
        else:
            return func(*args)

    return checker
@require_ints
def add_three(a, b, c):
    return a + b + c

print(add_three(1, 2, 3))
print(add_three(1, "2", 3))
