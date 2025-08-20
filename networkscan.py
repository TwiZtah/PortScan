import socket
import sys
import time

def scan_port(target_ip, port):
    """Attempts to connect to a single port and reports its status."""
    try:
        # Create a new socket (AF_INET for IPv4, SOCK_STREAM for TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1) # Set a timeout of 1 second

        # Attempt to connect
        result = s.connect_ex((target_ip, port)) # connect_ex returns an error code

        if result == 0:
            print(f"Port {port}: Open")
      
        else:
             
            pass 
        s.close() # Close socket

    except socket.gaierror:
        print(f"Hostname could not be resolved.")
        return False # Indicate failure
    except socket.error:
        print(f"Could not connect to server.")
        return False # Indicate failure
    return True # Indicate success (whether port was open or not)


def main():
    if len(sys.argv) != 3:
        print("Usage: python simple_port_scanner.py <target_ip_or_hostname> <port_range>")
        print("Example: python simple_port_scanner.py scanme.nmap.org 1-100")
        sys.exit(1)

    target = sys.argv[1]
    port_range_str = sys.argv[2]

    try:
        # Resolve hostname to an IP address
        target_ip = socket.gethostbyname(target)
        print(f"Scanning target: {target_ip}")

        # Parse the port range (e.g., "1-100")
        port_start, port_end = map(int, port_range_str.split('-'))

        start_time = time.time()

        # Loop ports and scan
        for port in range(port_start, port_end + 1):
            scan_port(target_ip, port)

        end_time = time.time()
        print(f"\nScan finished in {end_time - start_time:.2f} seconds.")

    except ValueError:
        print("Invalid port range format. Use <start>-<end> (e.g., 1-100).")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()