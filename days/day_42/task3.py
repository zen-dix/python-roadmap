class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector2D(x={self.x}, y={self.y})"

    def __add__(self, v2):
        if not isinstance(v2, Vector2D):
            return NotImplemented
        new_x = v2.x + self.x
        new_y = v2.y + self.y
        return Vector2D(new_x, new_y)


v1 = Vector2D(1, 4)
v2 = Vector2D(5, 2)
v3 = v1 + v2

print(str(v3))
print(repr(v3))
