class DataPacket:
    def __init__(self, content: str, source_ip: str):
        self.content = content
        self.source_ip = source_ip

    def __len__(self):
        return len(self.content)

    def __add__(self, d2):
        if not isinstance(d2, DataPacket):
            return NotImplemented
        elif not d2.source_ip == self.source_ip:
            raise ValueError()
        new_str = self.content + d2.content
        return DataPacket(new_str, self.source_ip)


p1 = DataPacket("auth_success", "192.168.1.5")
p2 = DataPacket("_session_expired", "192.168.1.5")
p3 = DataPacket("attack_payload", "10.0.0.1")

combined = p1 + p2
print(combined.content)
