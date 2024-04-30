
import socket

HOST = 'localhost'
PORT = 12345 

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))
#client_socket.sendall("encyrption key is 5".encode())
#received_key = client_socket.recv(1024)
#print(received_key.decode())
a = int(input("Enter a : "))
b = int(input("Enter b : "))
x = int(input("Enter x : "))
public_key = (a**x)%b
client_socket.sendall(f"{public_key}".encode())
received_key = int(client_socket.recv(1024).decode())
private_key = (received_key**x)%b
print("shared key is", private_key)

print(f"Connected to {HOST}:{PORT}")

# Send and receive data in a loop
while True:
    # Send data to the server
    message = input("Enter message to send (type 'exit' to quit): ")
    if message.lower() == 'exit':
        break
    client_socket.sendall(message.encode())

    # Receive response from the server
    response = client_socket.recv(1024)
    print("Received response:", response.decode())

# Close the client socket
client_socket.close()
