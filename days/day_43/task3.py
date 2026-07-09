class NginxConfig:
    def __init__(self, domain: str, workers: int):
        self.domain = domain
        self.workers = workers

    @property
    def workers(self):
        return self._workers

    @workers.setter
    def workers(self, value: int):
        if not isinstance(value, int):
            try:
                value = int(value)

            except ValueError:
                print("Warning: Invalid worker count. Set to 1.")
                value = 1
        self._workers = value
        if value > 16:
            self._workers = 16


conf = NginxConfig("zendix", 4)
conf.workers = 32
conf.workers = "8"
conf.workers = "many"
print(conf.workers)
