class LinuxProcess:
    def __init__(self, pid, name):
        self.pid = pid
        self.name = name
        self.status = "running"

    def kill(self):
        self.status = "terminated"
        print(f"Process {self.name} (PID: {self.pid}) killed")

process = LinuxProcess(4096, "nginx")
process.kill()