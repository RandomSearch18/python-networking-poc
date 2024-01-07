import socket
from zeroconf import ServiceInfo, Zeroconf

from common.constants import SERVER_PORT, ZEROCONF_SERVICE_TYPE


def advertise_service():
    # Get the local IP address
    our_ip_address = socket.gethostbyname(socket.gethostname())

    # Set up service information
    service_name = "MeganopolyServer"
    service_type = ZEROCONF_SERVICE_TYPE
    port = SERVER_PORT  # Inspired by Terraria's server port

    # Create a Zeroconf object
    zeroconf = Zeroconf()

    # Create a service info object to advertise the server
    service_info = ServiceInfo(
        service_type,
        f"{service_name}.{service_type}",
        addresses=[socket.inet_aton(our_ip_address)],
        port=port,
        properties={},
    )

    # Register the service
    zeroconf.register_service(service_info)

    # Keep the server running
    try:
        input(f"Advertising server on {our_ip_address}, port {port}")
    finally:
        zeroconf.unregister_service(service_info)
        zeroconf.close()


def main():
    advertise_service()
