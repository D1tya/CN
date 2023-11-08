import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('0.0.0.0', 12345))  


server_socket.listen(1)
print("Server is listening for incoming connections...")

client_socket, client_address = server_socket.accept()
print("Accepted connection from", client_address)

filename = client_socket.recv(1024).decode()

with open(filename, 'wb') as file:
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        file.write(data)

client_socket.close()
server_socket.close()


import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_address = ('server_ip_here', 12345)  
client_socket.connect(server_address)

filename = 'file_to_send.txt' 
client_socket.send(filename.encode())

with open(filename, 'rb') as file:
    data = file.read(1024)
    while data:
        client_socket.send(data)
        data = file.read(1024)

client_socket.close()
