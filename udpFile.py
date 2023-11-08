import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('0.0.0.0', 12345)  
server_socket.bind(server_address)

filename, client_address = server_socket.recvfrom(1024)
filename = filename.decode()

with open(filename, 'wb') as file:
    while True:
        data, client_address = server_socket.recvfrom(1024)
        if not data:
            break
        file.write(data)

server_socket.close()

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('server_ip_here', 12345) 

filename = 'file_to_send.txt'  
client_socket.sendto(filename.encode(), server_address)


with open(filename, 'rb') as file:
    while True:
        data = file.read(1024)
        if not data:
            break
        client_socket.sendto(data, server_address)


client_socket.close()
