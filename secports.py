import socket
import logging
from concurrent.futures import ThreadPoolExecutor

def check_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            logging.info(f"Port {port} is open on {target}")
        sock.close()
    except Exception as e:
        logging.error(f"Error scanning port {port} on {target}: {e}")

def scan_target(target, start_port, end_port):
    logging.info(f"Scanning target {target} from port {start_port} to {end_port}...")
    try:
        socket.gethostbyname(target)
    except socket.error as e:
        logging.error(f"Error resolving target {target}: {e}")
        return

    with ThreadPoolExecutor(max_workers=20) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(check_port, target, port)

if __name__ == "__main__":
    print("""
    Welcome to SecPorts

                                       `
                              (         (
                               )      (
                             )          )
                            (          ( ,
                           _ _)_      .-Y.
                .--._ _.--'.',T.\_.--' (_)`.
              .'_.   `  _.'  `-'    __._.--;
             /.'  `.  -'     ___.--' ,--.  :       o       ,-. _
            : |  xX|       ,'  .-'`.(   |  '      (   o  ,' .-' `,
           :  `.  .'    ._'-,  \   | \  ||/        `.{  / .'    :
          .;    `'    ,',\|\|   \  |  `.;'     .__(()`./.'  _.-'
          ;           |   ` `    \.'|\\ :      ``.-. _ '_.-'
         .'           ` /|,         `|\\ \        -'' \  \
         :             \`/|,-.       `|\\ :         ,-'| `-.
         :        _     \`/  |   _   .^.'\ \          -'> \_
         `;      --`-.   \`._| ,' \  |  \ : \           )`.\`-
          :.      .---\   \   ,'   | '   \ : .          `  `.\_,/
           :.        __\   `. :    | `-.-',  :               `-'
           `:.     -'   `.   `.`---'__.--'  /
            `:         __.\    `---'      _'
             `:.     -'    `.       __.--'
              `:.          __`--.--'\
    
    """)

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    target = input("Enter IP address or domain: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    scan_target(target, start_port, end_port)
