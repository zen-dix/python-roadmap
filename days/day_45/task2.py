class Route:
    def __init__(self, path: str, method: str):
        self.path = path
        self.method = method

    def __eq__(self, other):
        if not isinstance(other, Route):
            return NotImplemented
        return self.path == other.path and self.method == other.method

    def __hash__(self):
        return hash((self.path, self.method))

    def __repr__(self):
        return f"[{self.method}] {self.path}"


route1 = Route("/api/users", "GET")
route2 = Route("/api/users", "GET")
route3 = Route("/api/users", "POST")

routes_set = {route1, route2, route3}
print(routes_set)
