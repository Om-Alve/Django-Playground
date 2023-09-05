
import socket

mysoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('localhost', 9000)
mysoc.connect(server_address)

# Construct the HTTP request (using HTTP/1.1)
cmd = "GET HTTP/1.1\r\n\r\n".encode()

# Send the request
mysoc.send(cmd)

# Receive and print the response
while True:
    data = mysoc.recv(512)
    if len(data) <= 0:
        break
    print(data.decode('utf-8'), end='')

# Close the socket
mysoc.close()
