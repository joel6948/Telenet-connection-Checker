import telnetlib
import sys

def check_telnet_connection(host, port):
    try:
        # Create a Telnet object
        tn = telnetlib.Telnet(host, port, timeout=10)
        tn.close()
        return True
    except Exception:
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python telnet.py <file>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Strip whitespace and split by comma
                line = line.strip()
                if line:
                    try:
                        # Split the line into host and ports
                        parts = line.split(',')
                        host = parts[0].strip()
                        ports = [int(port.strip()) for port in parts[1:]]
                        
                        # Check each port for the given host
                        for port in ports:
                            if check_telnet_connection(host, port):
                                print(f"{host},{port}=connected")
                            else:
                                print(f"{host},{port}=not connected")
                    except ValueError:
                        print(f"Invalid line format: {line}. Expected format: <host>,<port1>,<port2>,...")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
