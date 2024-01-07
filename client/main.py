import socket
from zeroconf import ServiceListener, Zeroconf, ServiceBrowser

from common.constants import ZEROCONF_SERVICE_TYPE


class ServerListener(ServiceListener):
    def remove_service(self, zeroconf, type, name):
        print(f"Meganopoly server is gone! ({name})")

    def add_service(self, zeroconf: Zeroconf, type: str, name: str):
        info = zeroconf.get_service_info(type, name)
        if info:
            print(f"\nFound Meganopoly server! ({name})")
            print(f"Server address: {socket.inet_ntoa(info.addresses[0])} (port {info.port})")

    def update_service(self, zeroconf, type, name):
        pass


def discover_servers():
    zeroconf = Zeroconf()
    listener = ServerListener()

    # Browse for services of a specific type (same service type as used for advertising)
    browser = ServiceBrowser(zeroconf, ZEROCONF_SERVICE_TYPE, listener)

    try:
        input("Searching for servers...\n")
    finally:
        zeroconf.close()


def main():
    discover_servers()
