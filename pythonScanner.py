#!/bin/python3


# Import required modules
import sys                # For handling command-line arguments and exiting
import socket             # For creating network connections
from datetime import datetime  # To print the current time

# Check if the user has provided exactly one argument (the target IP/hostname)
if len(sys.argv) == 2:
    # Convert the provided hostname to an IP address
    target = socket.gethostbyname(sys.argv[1])
else:
    # If the number of arguments is incorrect, show usage instructions
    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py <ip>")
    sys.exit()  # Exit the program

# Print a banner with scan information
print("-" * 50)
print(f"Scanning Target: {target}")  # Show which target is being scanned
print(f"Time Started: {datetime.now()}")  # Show current date and time
print("-" * 50)

try:
    # Loop through ports 50 to 84 (inclusive)
    for port in range(50, 85):
        # Create a new socket for each port scan
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set default timeout for socket connections (1 second)
        socket.setdefaulttimeout(1)

        # Attempt to connect to the target IP and current port
        result = s.connect_ex((target, port))  # Returns 0 if port is open

        if result == 0:
            # If port is open, print it
            print(f"Port {port} is open")

        # Close the socket connection to free resources
        s.close()

# Handle keyboard interruption (Ctrl+C)
except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()

# Handle errors if the hostname cannot be resolved
except socket.gaierror:
    print("\nHostname could not be resolved.")
    sys.exit()

# Handle errors if the target is unreachable
except socket.error:
    print("Couldn't connect to server.")
    sys.exit()

