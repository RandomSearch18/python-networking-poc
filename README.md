# Python networking PoC

Testing ideas for client-server communicaton for Pygame games, specifically:
- Socket.io for low-latency data sync
    - Clients send actions to the server (like a HTTP request in REST APIs)
    - Server sends "updates" (like events in Discord's API) to clients
- Zeroconf for server discovery
    - This better work on the school network