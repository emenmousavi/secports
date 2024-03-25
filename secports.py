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

def get_int_input(prompt, min_val=None, max_val=None):
    """
    Get integer input from user with optional validation.
    """
    while True:
        try:
            val = int(input(prompt))
            if (min_val is not None and val < min_val) or (max_val is not None and val > max_val):
                print(f'Invalid input. Enter a value between {min_val} and {max_val}.')
            else:
                return val
        except ValueError:
            print('Invalid input. Enter a number.')

def main():
    ip = input('Enter the IP address or domain: ')
    print('Choose an option:')
    print('1. Check a special port')
    print('2. Check a port range')
    print('3. Check the first 1000 ports')
    option = get_int_input('Enter the option number: ', 1, 3)
    if option == 1:
        port = get_int_input('Enter the port number: ')
        if check_port(port, ip):
            print(f'Port {port} is open')
        else:
            print(f'Port {port} is closed')
    elif option == 2:
        start = get_int_input('Enter the start of the range: ')
        end = get_int_input('Enter the end of the range: ')
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
