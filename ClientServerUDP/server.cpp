#include <iostream>
#include <sys/socket.h>
#include <netinet/in.h>
#include <cstring>
#include <unistd.h>

using namespace std;

const int PORT = 9734;

int main() {
    int server_sockfd, client_sockfd;
    int server_len;
    socklen_t client_len;
    char buffer[1024];
    struct sockaddr_in servaddr, cliaddr;

    // criação do socket
    server_sockfd = socket(AF_INET, SOCK_DGRAM, 0);
    if (server_sockfd < 0) {
        cerr << "Error creating socket" << endl;
        exit(1);
    }

    // atribuindo informações ao endereço do servidor
    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = htonl(INADDR_ANY);
    servaddr.sin_port = htons(PORT);

    // associando o socket ao endereço do servidor
    if (bind(server_sockfd, (const struct sockaddr *)&servaddr, sizeof(servaddr)) < 0) {
        cerr << "Bind failed" << endl;
        exit(1);
    }
    
    while (true) 
    {
    	int data;
    	client_len = sizeof(cliaddr);
    	
    	cout << "Servidor esperando..." << endl;
    	
		// Receive from client
		ssize_t r = recvfrom(server_sockfd, &data, sizeof(data), 0, (struct sockaddr *)&cliaddr, &client_len);
        if(r < 0){
        	perror(" erro no recvfrom()");
            exit(1);
        }

        // Send response back to client
        ssize_t s = sendto(server_sockfd, &data, sizeof(data), 0, (struct sockaddr *)&cliaddr, client_len);
        if (s < 0)
        {
            printf("erro no sendto()");
            exit(1);
        }
        cout << "Resposta enviada." << endl;
    }

    //close(server_sockfd);
    return 0;
}

