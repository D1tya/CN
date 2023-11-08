import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 12345

server_socket.bind((host, port))

server_socket.listen(5)

print("Server is waiting for a connection...")

client_socket, addr = server_socket.accept()

print("Got a connection:",addr)

message = "Say Hello to Each Other"
client_socket.send(message.encode('utf-8'))

client_socket.close()
server_socket.close()

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 12345

client_socket.connect((host, port))

message = client_socket.recv(1024).decode('utf-8')

print(f"Received message: {message}")

client_socket.close()
