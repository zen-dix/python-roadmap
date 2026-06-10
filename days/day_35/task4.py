def require_ints(func):
    def wrapped(*args, **kwargs):
        for num in args:
            if not isinstance(num, int):
                return "Error: Only integers allowed"
        return func(*args)


    return wrapped
@require_ints
def multiply(*args):
    ans = 1
    for num in args:
        ans*=num
    return ans
print(multiply(2, 4.5, 5))