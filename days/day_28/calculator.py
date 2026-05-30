def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Ошибка: Деление на ноль"
print(divide(10,0))
