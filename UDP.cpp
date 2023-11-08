#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

int main() {
    int server_socket;
    char server_message[256] = "Hello from the UDP server!";
    struct sockaddr_in server_address, client_address;
    socklen_t client_address_length = sizeof(client_address);


    server_socket = socket(AF_INET, SOCK_DGRAM, 0);

    server_address.sin_family = AF_INET;
    server_address.sin_port = htons(9002);
    server_address.sin_addr.s_addr = INADDR_ANY;

    bind(server_socket, (struct sockaddr*)&server_address, sizeof(server_address));


    recvfrom(server_socket, server_message, sizeof(server_message), 0, (struct sockaddr*)&client_address, &client_address_length);
    printf("Received from client: %s\n", server_message);


    strcpy(server_message, "Hello from the UDP server!");
    sendto(server_socket, server_message, sizeof(server_message), 0, (struct sockaddr*)&client_address, client_address_length);

    close(server_socket);

    return 0;
}


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

int main() {
    int client_socket;
    char server_message[256] = "Hello from the UDP client!";
    struct sockaddr_in server_address;

    client_socket = socket(AF_INET, SOCK_DGRAM, 0);

    server_address.sin_family = AF_INET;
    server_address.sin_port = htons(9002);
    server_address.sin_addr.s_addr = INADDR_ANY;

    sendto(client_socket, server_message, sizeof(server_message), 0, (struct sockaddr*)&server_address, sizeof(server_address));

    recvfrom(client_socket, server_message, sizeof(server_message), 0, NULL, NULL);
    printf("Received from server: %s\n", server_message);
    close(client_socket);

    return 0;
}
