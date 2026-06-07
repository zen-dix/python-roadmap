import itertools
methods = ["get", "post", "put"]
statuses = [200, 404, 500]
formats = ["json", "xml"]

comb = list(itertools.product(methods, "-", statuses, "-", formats))
res = [" ".join(map(str, tup)) for tup in comb]
print(res)