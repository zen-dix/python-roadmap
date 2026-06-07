from itertools import chain, groupby
def group_by_node(*args):
    args = list(chain(*args))
    sorted_key = lambda x: x["node"]
    args.sort(key=sorted_key)
    for srv, d in groupby(args, key=sorted_key):
        print(srv, list(dct["ip"] for dct in list(d)))
b1 = [{"ip": "1.1.1.1", "node": "srv1"}, {"ip": "2.2.2.2", "node": "srv2"}]
b2 = [{"ip": "3.3.3.3", "node": "srv1"}, {"ip": "4.4.4.4", "node": "srv3"}]
group_by_node(b1, b2)
