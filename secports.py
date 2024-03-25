import socket

def check_port(port, ip='127.0.0.1'):
    """
    Check if a given port is open on a given IP address.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    if result == 0:
        return True
    else:
        return False

def check_port_range(start, end, ip='127.0.0.1'):
    """
    Check if any port in a given range is open on a given IP address.
    """
    for port in range(start, end+1):
        if check_port(port, ip):
            return True
    return False

def main():
    ip = input('Enter the IP address or domain: ')
    print('Choose an option:')
    print('1. Check a special port')
    print('2. Check a port range')
    print('3. Check the first 1000 ports')
    option = int(input('Enter the option number: '))
    if option == 1:
        port = int(input('Enter the port number: '))
        if check_port(port, ip):
            print(f'Port {port} is open')
        else:
            print(f'Port {port} is closed')
    elif option == 2:
        start = int(input('Enter the start of the range: '))
        end = int(input('Enter the end of the range: '))
        if check_port_range(start, end, ip):
            print(f'A port in the range {start}-{end} is open')
        else:
            print(f'No ports in the range {start}-{end} are open')
    elif option == 3:
        if check_port_range(1, 1000, ip):
            print('At least one of the first 1000 ports is open')
        else:
            print('None of the first 1000 ports are open')
    else:
        print('Invalid option')

if __name__ == '__main__':
    main()
