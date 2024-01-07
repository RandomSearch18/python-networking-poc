import socket
from zeroconf import Zeroconf, ServiceBrowser


class ServerListener:
    def remove_service(self, zeroconf, type, name):
        print(f"Service {name} removed")

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        if info:
            print(f"Discovered service: {name}")
            print(f"Server address: {socket.inet_ntoa(info.addresses[0])}")
            print(f"Server port: {info.port}")
            # You can add the discovered servers to a list or display them to the user

    def update_service(self, zeroconf, type, name):
        pass


def discover_servers():
    zeroconf = Zeroconf()
    listener = ServerListener()

    # Browse for services of a specific type (same service type as used for advertising)
    browser = ServiceBrowser(zeroconf, "_meganopoly._tcp.local.", listener)

    try:
        input("Searching for servers... Press Enter to stop.\n")
    finally:
        zeroconf.close()


if __name__ == "__main__":
    discover_servers()
