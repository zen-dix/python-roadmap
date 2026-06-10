def collect_logs(*args):
    args = sorted(set(args))
    return args
print(collect_logs("web1", "db_main", "web1", "cache_node"))
