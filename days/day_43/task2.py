class APIResponse:
    def __init__(self, status_code: int, data, message: str):
        self.status_code = status_code
        self.data = data
        self.message = message

    @classmethod
    def success(cls, data: dict):
        return cls(200, data, "Success")

    @classmethod
    def not_found(cls):
        return cls(404, None, "Resource not found")

    @classmethod
    def server_error(cls, error_msg: str):
        return cls(500, None, error_msg)

    def to_json(self):
        return {
            "status_code": self.status_code,
            "data": self.data,
            "message": self.message,
        }


resp1 = APIResponse.success({"user_id": 1})
resp2 = APIResponse.not_found()
resp3 = APIResponse.server_error("Database connection failed")

print(resp1.to_json())
print(resp2.to_json())
print(resp3.to_json())
