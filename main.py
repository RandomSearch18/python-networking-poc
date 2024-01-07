"""Wrapper script for the client and server programs

Usage:
- python main.py client
- python main.py server
"""

import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py client|server")
        sys.exit(1)

    if sys.argv[1] == "client":
        from client.main import main

        main()
    elif sys.argv[1] == "server":
        from server.main import main

        main()
    else:
        print("Usage: python main.py client|server")
        sys.exit(1)
