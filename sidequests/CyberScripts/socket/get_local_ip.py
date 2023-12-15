import socket


def get_local_ip():
    try:
        # Create a socket object to get local machine name
        host_name = socket.gethostname()

        # Get the IP address of the local machine
        ip_address = socket.gethostbyname(host_name)

        print(f"Local IP Address: {ip_address}")
    except socket.error as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    get_local_ip()
