import socket

def scan(ip, first_port, last_port):
    print(f"Scanning {last_port - first_port} ports on {ip}")
    for port in range(first_port, last_port):
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.settimeout(3)
        connection_result = connection.connect_ex((ip, port))
        if connection_result == 0:
            print(f"Port {port}: Open")
        connection.close()

if __name__ == "__main__":
    ip = input("Enter an IP to scan: ")
    first_port = input("Enter the first port to scan: ")
    last_port = input("Enter the last port to scan: ")
    scan(ip, int(first_port), int(last_port))

#192.168.1.100
#15
#30
#Port 22: Open