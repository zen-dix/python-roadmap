class EmailService:
    def send(self, user, text):
        return f"Email to {user}: {text}"


class SMSService:
    def send(self, user, text):
        return f"SMS to {user}: {text}"


class AlertSystem:
    def __init__(self):
        self.services = []

    def add_service(self, service):
        self.services.append(service)

    def broadcast(self, user, text):
        for service in self.services:
            print(service.send(user, text))


alerts = AlertSystem()
alerts.add_service(EmailService())
alerts.add_service(SMSService())
alerts.broadcast("zendix", "Server overload!")
