
def filter_logs(logs_list, **kwargs):

    for dct in logs_list:
        if all(dct.get(key) == value for key, value in kwargs.items()):
            print(dct)
data = [
    {"method": "GET", "status": 200, "user": "admin"},
    {"method": "POST", "status": 403, "user": "guest"},
    {"method": "GET", "status": 200, "user": "guest"}
]
filter_logs(data, method="GET", status=200)