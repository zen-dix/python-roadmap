class Report:
    def generate(self, timestamp: str):
        raise NotImplementedError()


class MetricsReport(Report):
    def generate(self, timestamp: str):
        print(f"[Metrics] Generating CPU and RAM usage log at {timestamp}")


class SecurityReport(Report):
    def generate(self, timestamp: str):
        print(f"[Security] Scanning access logs and firewall rules at {timestamp}")


class ReportEngine:
    def __init__(self, reports: list):
        self.reports = reports

    def run_all(self, timestamp: str):
        for report in self.reports:
            report.generate(timestamp)


timestamp = "2026-07-06 08:30:00"
reports = [MetricsReport(), SecurityReport()]
report = ReportEngine(reports)
report.run_all(timestamp)
