import itertools

class LoadBalancer:
    def __init__(self, ip):
        self.server_pool = itertools.cycle(ip)

    def get_next_server(self):
        return next(self.server_pool)

servers = LoadBalancer(["192.168.1.1", "192.168.1.2", "192.168.1.3"])
for i in range(5):
    print(servers.get_next_server())