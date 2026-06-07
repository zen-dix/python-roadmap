#недоделал
from itertools import chain, groupby
from task3 import filter_logs
def analyze_traffic(*args, **kwargs):
    args = list(chain(*args))
    filter_logs(args)
s1 = [{"service": "auth", "endpoint": "/login", "time_ms": 120}, {"service": "db", "endpoint": "/query", "time_ms": 300}]
s2 = [{"service": "auth", "endpoint": "/login", "time_ms": 80}, {"service": "auth", "endpoint": "/logout", "time_ms": 40}]
analyze_traffic(s1, s2, service="auth")