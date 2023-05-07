#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <stdlib.h>
#include <iostream>
#include <string.h>
#include <sys/time.h>
#include <fstream>
#include <vector>
#include <cmath>

using std::cout;
using std::endl;

const int PORT = 9734;
const int NUM_TRIALS = 30;

// args: argv[1] = ip, argv[2] = package_size
int main(int argc, char *argv[]) {
	if (argc < 3)
    {
        cout << "Usage: ./client <ip> <package_size>" << endl;
        return 0;
    }
    
	int sockfd;
	int len;
	socklen_t len_recv;
	struct sockaddr_in addr;
	int package_size = atoi(argv[2]);
    char buffer[package_size];
    struct timeval start, end, timeout;
    std::vector<double> times(NUM_TRIALS);
	
	// criação do socket 
    sockfd = socket(AF_INET, SOCK_DGRAM, 0);
    if (sockfd < 0) {
        std::cerr << "Error opening socket" << std::endl;
        exit(1);
    }
	
	// atribuindo informações ao endereço do cliente
    addr.sin_family = AF_INET;
    addr.sin_addr.s_addr = inet_addr(argv[1]);
    addr.sin_port = htons(PORT);
    
    len = sizeof(addr);
    len_recv = sizeof(addr);
    
    // Configurando timeout para 3 segundos
    timeout.tv_sec = 3; 
    timeout.tv_usec = 0;
    
    // Preenchendo buffer
    memset(buffer, 'a', package_size);
    
	// iterando NUM_TRIALS vezes para cada tamanho de pacote
    for (int i = 0; i < NUM_TRIALS; i++) 
    {
   		if (setsockopt(sockfd, SOL_SOCKET, SO_RCVTIMEO, (char *)&timeout, sizeof(timeout)) < 0)
        {
            cout << "setsockopt failed" << endl;
            return 1;
        }
		
        gettimeofday(&start, NULL); // começa a contar o tempo
        // envia dados para o servidor
        ssize_t s = sendto(sockfd, buffer, sizeof(buffer), 0, (struct sockaddr*) &addr, len);
		if (s == -1)
        {
            cout << "sendto failed" << endl;
            close(sockfd);
            return 1;
        }
        
        // recebe dados do servidor
		ssize_t r = recvfrom(sockfd, buffer, sizeof(buffer), 0, (struct sockaddr *)&addr, &len_recv);
		if (r == -1)
        {
            if (errno == EAGAIN || errno == EWOULDBLOCK)
            {
                cout << "Timeout reached. No data received." << endl;
                exit(1);
            }
            else
            {
                cout << "recvfrom failed" << endl;
            }
        }
        else
        {
        	gettimeofday(&end, NULL); // finaliza a contagem do tempo
			times[i] = (end.tv_sec - start.tv_sec) * 1000000.0 + (end.tv_usec - start.tv_usec);
        }
    }

    // Calculo da média e desvio padrão dos tempos
	double sum = 0;
	for (int j = 0; j < NUM_TRIALS; j++){
		sum += times[j];
	}
    double mean = sum / NUM_TRIALS;
    std::cout << "Tempo médio para " << package_size << " bytes = " << mean << " microsegundos" << std::endl;
    
    double variance = 0;
    for (int j = 0; j < NUM_TRIALS; j++){
    	variance += pow(times[j] - mean, 2);
    }
    variance /= NUM_TRIALS;
    double std_dev = sqrt(variance);
    std::cout << "Desvio padrão para: " << package_size << " bytes = " << std_dev << " microsegundos" << std::endl;
    
    return 0;
}

