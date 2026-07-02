class ServerSession:
    def __init__(self):
        self.__ip_adress = None

    def set_ip_address(self, new_ip):
        if new_ip.count(".") == 3:
            self.__ip_adress = new_ip
            print(f"Session IP updated to {self.__ip_adress}")

        else:
            print("Error: Invalid IP format specified.")


server1 = ServerSession()
ip1 = input()
server1.set_ip_address(ip1)
