def log_api_arguments(func):
    def wrapper(*args, **kwargs):
        for param, log in kwargs.items():
            print(f"Param: {param} = {log}")
        return func(*args, **kwargs)

    return wrapper


@log_api_arguments
def configure_route(route_path, **kwargs):
    return f"Route {route_path} configured."


configure_route("/api/v1/users", method="POST", secure=True)
