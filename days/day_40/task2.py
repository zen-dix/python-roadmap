class BaseModel:
    _table_name = "base"

    def save(self):
        return f"Saving data to table: {self._table_name}"


class User(BaseModel):
    _table_name = "users"

    def __init__(self, username):
        self.username = username


class Product(BaseModel):
    _table_name = "products"

    def __init__(self, price):
        self.price = price


user = User("zendix")
product = Product(99.9)

print(user.save())
print(product.save())
