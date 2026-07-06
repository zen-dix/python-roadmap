class BaseNotifier:
    def send(self, user_id: int, message: str):
        raise NotImplementedError()


class EmailNotifier(BaseNotifier):
    def send(self, user_id: int, message: str):
        print(f"[Email] Sending to user {user_id}: {message}")


class PushNotifier(BaseNotifier):
    def send(self, user_id: int, message: str):
        print(f"[Push] Sending to user {user_id}: {message}")


class TelegramNotifier(BaseNotifier):
    def send(self, user_id: int, message: str):
        print(f"[Telegram] Sending to user {user_id}: {message}")


class NotificationService:
    def __init__(self, *args):
        self.providers = args

    def broadcast(self, user_id: int, message: str):
        for provider in self.providers:
            provider.send(user_id, message)


service = NotificationService(EmailNotifier(), PushNotifier(), TelegramNotifier())
service.broadcast(42, "Server reboot in 5 minutes.")
