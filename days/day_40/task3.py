class CacheAdapter:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def ping(self):
        return f"Pinging {self.host}:{self.port}..."


class RedisCache(CacheAdapter):
    def __init__(self, host, port, db_index):
        super().__init__(host, port)
        self.db_index = db_index

    def set_key(self, key, value):
        return f"Redis [{self.db_index}]: {key} -> {value}"


class MemcachedCache(CacheAdapter):
    def __init__(self, host, port, memory_limit):
        super().__init__(host, port)
        self.memory_limit = memory_limit

    def allocate(self):
        return f"Allocated {self.memory_limit}MB"
