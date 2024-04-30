
import socket

HOST = '0.0.0.0'  # Listen on all available network interfaces
PORT = 12345  # Choose a port number (make sure it's not already in use)

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen()

# Accept incoming connections in a loop
while True:
    # Accept incoming connections
    client_socket, client_address = server_socket.accept()
    
    print(f"Connection from {client_address}")

    print(f"Server listening on {HOST}:{PORT}")
    a = int(input("Enter a : "))
    b = int(input("Enter b : "))
    x = int(input("Enter x : "))
    public_key = (a**x)%b
    client_socket.sendall(f"{public_key}".encode())
    received_key = int(client_socket.recv(1024).decode())
    shared_key = (received_key**x)%b
    print("Shared key : ", shared_key)

    # Receive data from the client
    while True:
        data = client_socket.recv(1024)
        if not data:
            # If no more data is received, break the loop
            client_socket.close()
            server_socket.close()
            break
        print(f"Received data from {client_address}: {data.decode()}")
        
        # You can add your processing logic here
        
        # Echo the received data back to the client
        client_socket.sendall(data)
    # Close the client socket
    client_socket.close()
