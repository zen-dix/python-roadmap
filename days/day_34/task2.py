from itertools import groupby

logs = [("500", "/api/users"), ("404", "/api/items"), ("500", "/api/auth"), ("200", "/"), ("404", "/favicon.ico")]
sort_key = lambda x: x[0]
sorted_logs = sorted(logs, key=sort_key)

for err, l in groupby(sorted_logs, key=sort_key):
    print(err, len(list(l)))