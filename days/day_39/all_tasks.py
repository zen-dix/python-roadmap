class UserSession:
    def __init__(self, username):
        self.username = username
        self.request_history = []

    def add_request(self, endpoint):
        self.request_history.append(endpoint)
        print(f"[{self.username}] Request added. Total: {len(self.request_history)}")


class AppConfig:
    default_timeout = 30
    max_connections = 100

    def __init__(self, app_name):
        self.app_name = app_name

    def show_config(self):
        print(
            f"Config for {self.app_name}: timeout={self.default_timeout}, max_conn={self.max_connections}"
        )


class DatabaseConnection:
    active_connections = 0
    MAX_CONNECTIONS = 3

    def __init__(self):
        if DatabaseConnection.active_connections >= DatabaseConnection.MAX_CONNECTIONS:
            print("Error: Connection limit reached!")
        else:
            DatabaseConnection.active_connections += 1
            print(
                f"Connection established. Active: {DatabaseConnection.active_connections}"
            )

    def close_connection(self):
        DatabaseConnection.active_connections -= 1


class RateLimiter:
    blacklisted_ips = []

    def __init__(self, endpoint_name):
        self.endpoint_name = endpoint_name
        self.requests_db = {}

    def make_request(self, ip_adress):
        if ip_adress in RateLimiter.blacklisted_ips:
            print(f"[{self.endpoint_name}] 403 Forbidden: IP is blacklisted")
        else:
            if self.requests_db.get(ip_adress, 0) >= 3:
                print(f"[{self.endpoint_name}] 429 Too Many Requests: Blacklisting IP")
                RateLimiter.blacklisted_ips.append(ip_adress)
            else:
                self.requests_db[ip_adress] = self.requests_db.get(ip_adress, 0) + 1

            print(f"[{self.endpoint_name}] 200 OK: Request processed")


# task 1
user1 = UserSession("gleb")
user2 = UserSession("admin")

user1.add_request("/home")
user2.add_request("/settings")
user1.add_request("/api/v1/data")
# task 2
app1 = AppConfig("AuthService")
app2 = AppConfig("PaymentService")

AppConfig.default_timeout = 45
app1.show_config()
app2.show_config()


# task 3
app2.default_timeout = 60
AppConfig.default_timeout = 10

app1.show_config()
app2.show_config()

# task 4
conn1 = DatabaseConnection()
conn2 = DatabaseConnection()
conn3 = DatabaseConnection()
conn4 = DatabaseConnection()
conn2.close_connection()
conn5 = DatabaseConnection()

# task 5
api_login = RateLimiter("/login")
api_data = RateLimiter("/data")

# Simulate traffic
api_login.make_request("192.168.1.10")
api_login.make_request("192.168.1.10")
api_login.make_request("192.168.1.10")
api_login.make_request("192.168.1.10")  # Blacklists here
api_data.make_request("192.168.1.10")  # Should be 403 because of global blacklist
