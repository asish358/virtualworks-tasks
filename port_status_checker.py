import socket

def check_port(host, port):
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)

        # Attempt to connect
        result = s.connect_ex((host, port))

        if result == 0:
            print(f"Port {port} on {host} is OPEN.")
        else:
            print(f"Port {port} on {host} is CLOSED.")

        s.close()

    except socket.gaierror:
        print("Hostname could not be resolved.")
    except Exception as e:
        print("Error:", e)

def main():
    print("=== Port Status Checker ===")

    host = input("Enter Hostname/IP Address: ")
    
    try:
        port = int(input("Enter Port Number: "))
        check_port(host, port)
    except ValueError:
        print("Please enter a valid port number.")

if __name__ == "__main__":
    main()
