class ServiceApiKey:
    def __init__(self, service_name, api_key):
        self.service_name = service_name
        self.__api_key = api_key

    def get_masked_key(self):
        ans = self.__api_key[:4] + (len(self.__api_key) - 4) * "*"
        return ans


key_storage = ServiceApiKey("S3_Storage", "aws_secret_key_prod_99812")
print(key_storage.service_name)
print(key_storage.get_masked_key())
