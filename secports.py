import socket
import logging
from concurrent.futures import ThreadPoolExecutor

def check_port(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                logging.info(f"Port {port} is open on {target}")
    except Exception as e:
        logging.error(f"Error scanning port {port} on {target}: {e}")

def scan_target(target, start_port, end_port):
    logging.info(f"Scanning target {target} from port {start_port} to {end_port}...")
    with ThreadPoolExecutor(max_workers=20) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(check_port, target, port)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    target = input("Enter IP address or domain: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    scan_target(target, start_port, end_port)
