
class UserSession:
    def __init__(self, user_id, token):
        self.user_id = user_id
        self.token = token
        self.is_active = True

obj = UserSession(101, "abc-123")
print(obj.is_active)
