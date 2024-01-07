import socket
from zeroconf import ServiceInfo, Zeroconf


def advertise_service():
    # Get the local IP address
    ip_address = socket.gethostbyname(socket.gethostname())

    # Set up service information
    service_name = "MeganopolyServer"
    service_type = "_meganopoly._tcp.local."  # Service type, you can define your own
    port = 7777  # Inspired by Terraria's server port

    # Create a Zeroconf object
    zeroconf = Zeroconf()

    # Create a service info object to advertise the server
    service_info = ServiceInfo(
        service_type,
        f"{service_name}.{service_type}",
        addresses=[socket.inet_aton(ip_address)],
        port=port,
        properties={},
    )

    # Register the service
    zeroconf.register_service(service_info)

    # Keep the server running
    try:
        input("Server advertising... Press Enter to stop.")
    finally:
        zeroconf.unregister_service(service_info)
        zeroconf.close()


if __name__ == "__main__":
    advertise_service()
