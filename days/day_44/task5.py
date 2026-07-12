class Cache:
    def __init__(self):
        self.storage = {}

    def set(self, key, value):
        self.storage[key] = value
        return self.storage.get(key)

    def get(self, key):
        return self.storage.get(key, None)


class NetworkClient:
    def fetch(self, url):
        print(f"Making network request to {url}")
        return f"Data from {url}"


class CachedAPI:
    def __init__(self, cache: Cache, network: NetworkClient):
        self.cache = cache
        self.network = network

    def get_data(self, url):
        if self.cache.get(url):
            print("Fetching from cache")
            return self.cache.get(url)
        else:
            value = self.network.fetch(url)
            return self.cache.set(url, value)


cache = Cache()
network = NetworkClient()
api = CachedAPI(cache, network)

print(api.get_data("api.github.com/users"))
print("-" * 20)
print(api.get_data("api.github.com/users"))
