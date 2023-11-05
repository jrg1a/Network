import socket

def is_host_alive(target):
    """
    Check if the host is alive using a ping-like method.
    """
    try:
        # This will check if the host is valid and reachable by translating the name.
        ip = socket.gethostbyname(target)
        return True
    except socket.gaierror:
        return False

def scan_ports(target, start_port, end_port):
    """
    Scan ports in the range [start_port, end_port] for a given target.
    """
    open_ports = []

    for port in range(start_port, end_port + 1):
        print(f"Scanning port {port}...", end='\r')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        s.close()

    return open_ports

def main():
    target = input("Enter the target (IP/Hostname): ")
    if not is_host_alive(target):
        print(f"Unable to reach {target}. Exiting.")
        return

    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))

    print(f"Scanning {target} for open ports...")
    open_ports = scan_ports(target, start_port, end_port)

    if open_ports:
        print(f"\nNumber of open ports on {target}: {len(open_ports)}")
        print(f"Open ports: {', '.join(map(str, open_ports))}")
    else:
        print(f"\nNo open ports on {target} in the range {start_port}-{end_port}.")

if __name__ == "__main__":
    main()
