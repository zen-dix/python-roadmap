class AppConfiguration:
    def __init__(self, config_dict):
        self._host = config_dict["host"]
        self._port = config_dict["port"]
        self.__jwt_secret = config_dict["jwt_secret"]

    def get_info_summary(self):
        return f"App running on {self._host}:{self._port}"

    def validate_security(self):
        if len(self.__jwt_secret) > 16:
            return True
        else:
            return False


config_payload = {"host": "0.0.0.0", "port": 5000, "jwt_secret": "short_secret"}
app_env = AppConfiguration(config_payload)
print(app_env.get_info_summary())
print(app_env.validate_security())
