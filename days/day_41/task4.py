class StorageAdapter:
    def save(self, key: str, value: str):
        raise NotImplementedError()

    def get(self, key: str):
        raise NotImplementedError()


class MemoryStorage(StorageAdapter):
    def __init__(self):
        self.storage = {}

    def save(self, key: str, value: str):
        self.storage[key] = value
        print(f"[Memory] Saved {key} -> {value}")

    def get(self, key: str):
        print(f"[Memory] Retrieved {key}: {self.storage.get(key)})")
        return self.storage.get(key)


class MockFileStorage(StorageAdapter):
    def __init__(self):
        self.disk_content = {}

    def save(self, key: str, value: str):
        self.disk_content[key] = value
        print(f"[File] Opening disk file... Saved {key} -> {value}")

    def get(self, key: str):
        print(f"[File] Opening disk file... {key}: {self.disk_content.get(key)}")
        return self.disk_content.get(key)


def app_logic(storage: StorageAdapter):
    storage.save("session_id", "abc-123")
    val = storage.get("session_id")
    print(f"Retrieved session_id: {val}")


app_logic(MemoryStorage())
app_logic(MockFileStorage())
