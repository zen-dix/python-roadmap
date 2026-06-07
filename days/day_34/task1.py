from itertools import chain
def merge_streams(*args):
    return list(chain(*args))
stream1 = ["auth_ok"]
stream2 = ["db_connect", "db_timeout"]
stream3 = ["cache_miss"]
print(merge_streams(stream1, stream2, stream3))