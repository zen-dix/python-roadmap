class Process:
    def __init__(self, name, pid):
        self.name = name
        self.pid = pid
proc_nginx = Process("nginx", 1024)
proc_postgres = Process("postgres", 2048)
print(f"Процесс [{proc_nginx.name}] запущес с PID [{proc_nginx.pid}].")
print(f"Процесс [{proc_postgres.name}] запущес с PID [{proc_postgres.pid}].")