#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <netdb.h>
#include <sys/socket.h>
#include <sys/select.h>
#include<stdbool.h>


int main(int argc, char *argv[])
{
	const char *port = "8088";		/* порт по умолчанию */
	char *host;
	struct addrinfo hints,*server;
	int r,sockfd,done;
	char buffer[BUFSIZ];
	fd_set read_fd;

	if( argc<2 )
	{
		fprintf(stderr,"Задайте адрес chat сервера.\n");
		exit(1);
	}
	host = argv[1];
    if (argc>2)
        port = argv[2];
    //printf("host = %s\n",host);
    //printf("Порт = %s\n",port);

	printf("Looking for chat server on %s...",host);
	memset( &hints, 0, sizeof(hints) );		// use memset_s() 
	hints.ai_family = AF_INET;				// IPv4 
	hints.ai_socktype = SOCK_STREAM;		// TCP 
	r = getaddrinfo( host, port, &hints, &server );
	if( r!=0 )
	{
		perror("failed");
		exit(1);
	}
	puts("found");

	// создаем socket 
	sockfd = socket(server->ai_family,server->ai_socktype,server->ai_protocol);
	if( sockfd==-1 )
	{
		perror("failed");
		exit(1);
	}

	// соединение to the socket 
	r = connect(sockfd,server->ai_addr,server->ai_addrlen);
	freeaddrinfo(server);
	if( r==-1 )
	{
		perror("failed");
		exit(1);
	}

	// цикл для опроса дискирипторов 
	done = false;
	while(!done)
	{
		// инициализируем   descriptor  
		FD_ZERO(&read_fd);
		FD_SET(sockfd, &read_fd);		// добавляем soccet 

		FD_SET(0, &read_fd);			// добавляем стандартный input
		r = select( sockfd+1, &read_fd, NULL, NULL, 0);
		if( r==-1 )
		{
			perror("failed");
			exit(1);
		}

		// получение из сервера
		if( FD_ISSET(sockfd, &read_fd) )
		{
			r = recv( sockfd, buffer, BUFSIZ, 0);
			if( r<1 )
			{
				puts("Connection closed by peer");
				break;
			}
			// увеличение буфера 
			buffer[r] = '\0';
			printf("%s",buffer);
		}

		// ввод 
        if( FD_ISSET(0, &read_fd) )
		{
			// Проверка на пустую строку
			if( fgets(buffer,BUFSIZ,stdin)==NULL )
			{
				putchar('\n');
			}
			// выход из цикла и чата 
			else if( strcmp(buffer,"close\n")==0 )
			{
				done=true;
			}
			else
			{
				send(sockfd,buffer,strlen(buffer),0);
			}
		}
	}	

	printf("Disconnected\nДосвидание!\n");
	close(sockfd);

	return(0);
}
