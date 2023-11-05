import socket
import threading
import time

def is_host_alive(target):
    try:
        ip = socket.gethostbyname(target)
        return True
    except socket.gaierror:
        return False

def grab_banner(ip, port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner.decode().strip()
    except:
        return None

def scan_port_range(target, start_port, end_port, open_ports, rate_limit):
    for port in range(start_port, end_port + 1):
        if rate_limit:
            time.sleep(rate_limit)  # Sleep for the rate limit duration.
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            banner = grab_banner(target, port)
            if banner:
                open_ports[port] = banner
            else:
                open_ports[port] = None
        s.close()

def main():
    target = input("Enter the target (IP/Hostname): ")
    if not is_host_alive(target):
        print(f"Unable to reach {target}. Exiting.")
        return

    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    rate_limit = float(input("Enter rate limit (seconds between scans, 0 for no limit): "))

    threads = []
    open_ports = {}
    thread_count = 10
    ports_per_thread = (end_port - start_port + 1) // thread_count

    for i in range(thread_count):
        start = start_port + i * ports_per_thread
        if i == thread_count - 1:
            end = end_port
        else:
            end = start + ports_per_thread - 1
        thread = threading.Thread(target=scan_port_range, args=(target, start, end, open_ports, rate_limit))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"\nScanning complete!")
    if open_ports:
        print(f"Open ports on {target}:")
        for port, banner in open_ports.items():
            if banner:
                print(f"{port}: {banner}")
            else:
                print(f"{port}")
    else:
        print(f"No open ports on {target} in the range {start_port}-{end_port}.")

if __name__ == "__main__":
    main()
