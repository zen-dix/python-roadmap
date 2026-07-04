class BaseConfig:
    def __init__(self, settings):
        self.settings = settings

    def get(self, key):
        return self.settings.get(key, None)


class EnvConfig(BaseConfig):
    def __init__(self, settings):
        new_settings = {k.upper(): v for k, v in settings.items()}
        super().__init__(new_settings)


class JSONConfig(BaseConfig):
    def get(self, key):
        ans = super().get(key)
        if ans == None:
            return f"Key {key} not found in JSON"
        else:
            return ans


env = EnvConfig({"debug": "true", "port": 8080})
print(env.get("DEBUG"))

json_conf = JSONConfig({"host": "localhost"})
print(json_conf.get("timeout"))
