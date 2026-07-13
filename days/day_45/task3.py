class NotificationSender:
    def send(self, message):
        raise NotImplementedError()


class EmailSender(NotificationSender):
    def __init__(self, address):
        self.adress = address

    def send(self, message):
        print(f"Sending EMAIL to {self.adress}: {message}")


class PushSender(NotificationSender):
    def __init__(self, device_id):
        self.device_id = device_id

    def send(self, message):
        print(f"Sending PUSH to {self.device_id}: {message}")


def broadcast_message(senders_list, message):
    for sender in senders_list:
        sender.send(message)


senders = [EmailSender("admin@test.com"), PushSender("device_id_8932")]
broadcast_message(senders, "Server is going down for maintenance")
