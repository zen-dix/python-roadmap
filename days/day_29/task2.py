def multiply(*args):
    ans = 1
    for num in args: ans*=num
    return ans
print(multiply(2, 4, 10))