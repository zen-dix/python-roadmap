def build_config(**kwargs):
    ans = ""
    kwargs = dict(sorted(kwargs.items(), key=lambda x: x[0]))
    for key, value in kwargs.items():
        if value is not None:
            ans += f'{key}="{value}";'
    return f'"{ans}"'
print(build_config(host="localhost", port=8080, debug=None, timeout=30))
