class PortScanner:
    def scan(self, target_ip, port):
        print(f"[+] Scanning {target_ip}:{port}...")
scanner = PortScanner()
scanner.scan("113.3.4.1", 80)
scanner.scan("342.4.43.2", 443)
