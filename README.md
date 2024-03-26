### SecPorts

SecPorts is a Python tool for scanning open ports on a target machine.

#### Requirements
- Python 3.x

#### Usage
1. Clone the repository:
   ```
   git clone https://github.com/your_username/SecPorts.git
   ```
2. Navigate to the SecPorts directory:
   ```
   cd SecPorts
   ```
3. Run the script:
   ```
   python secports.py
   ```
4. Follow the prompts to enter the target IP address or domain, start port, and end port.

#### Features
- Multi-threaded port scanning for faster results.
- Support for scanning a range of ports.
- Simple and easy-to-use command-line interface.
- Logging of open ports.
- Error handling for robustness.

#### Note
- This tool is for educational and testing purposes only. Ensure you have proper authorization before scanning any network.
- Adjust the maximum number of workers in the `ThreadPoolExecutor` according to your system resources and network limitations.
- Customize logging settings as needed for your environment.

Feel free to enhance the script or contribute to the repository!
