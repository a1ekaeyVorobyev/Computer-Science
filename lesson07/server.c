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

	char *port = "8088";					// порт для кликетов 
    if (argc>1)
        port = argv[1];
    //printf("Порт = %s\n",port);
	const int clientname_size = 32;				// для  клиентов IPv4 address
	char clientname[clientname_size];
	char buffer[BUFSIZ],sendstr[BUFSIZ];
	const int backlog = 10;						// количество max соединений
	char connection[backlog][clientname_size];	// сохрание  всех IPv4 сщужинений
	socklen_t address_len = sizeof(struct sockaddr);
	struct addrinfo hints,*server;
	struct sockaddr address;
	int r,max_connect,fd,x,done;
	fd_set main_fd,read_fd;
	int serverfd,clientfd;

	/* setup the server */
	memset( &hints, 0, sizeof(struct addrinfo));	
	hints.ai_family = AF_INET;			// IPv4 
	hints.ai_socktype = SOCK_STREAM;	// TCP 
	hints.ai_flags = AI_PASSIVE;		// принять любое соединение
	r = getaddrinfo( 0, port, &hints, &server );
	if( r!=0 )
	{
		perror("failed");
		exit(1);
	}

	/* create a socket */
	serverfd = socket(server->ai_family,server->ai_socktype,server->ai_protocol);
	if( serverfd==-1 )
	{
		perror("failed");
		exit(1);
	}

	r = bind(serverfd,server->ai_addr,server->ai_addrlen);
	if( r==-1 )
	{
		perror("failed");
		exit(1);
	}

	// Ckeiftv cоединения
	puts("Chat Server is listening...");
	r = listen(serverfd,backlog);
	if( r==-1 )
	{
		perror("failed");
		exit(1);
	}


	max_connect = backlog;		
	FD_ZERO(&main_fd);			// // инициализируем   descriptor  
	FD_SET(serverfd, &main_fd);	

	// Цикл для установки соединения
	done = false;
	while(!done)
	{

		read_fd = main_fd;
		
		r = select(max_connect+1,&read_fd, NULL, NULL, 0);
		if( r==-1 )
		{
			perror("failed");
			exit(1);
		}

		//Для активный соединений.
		for( fd=1; fd<=max_connect; fd++)
		{
			
			if( FD_ISSET(fd,&read_fd) )
			{
				//Проверка на новые соединеия
				if( fd==serverfd )
				{
					// Добавляем нового клиента
					clientfd = accept(
							serverfd,
							(struct sockaddr *)&address,
							&address_len
							);
					if( clientfd==-1 )
					{
						perror("failed");
						exit(1);
					}
					
					r = getnameinfo(
							(struct sockaddr *)&address,
							address_len,
							clientname,
							clientname_size,
							0,
							0,
							NI_NUMERICHOST
							);
					// Добавляем в массив новое соединение
					strcpy(connection[clientfd],clientname);

					// Добавляем новое соединение в дискриптор
					FD_SET(clientfd, &main_fd);


					strcpy(buffer,"SERVER> Welcome ");
					strcat(buffer,connection[clientfd]);
					strcat(buffer," to the chat server\n");
					strcat(buffer,"SERVER> Type 'close' to disconnect; 'shutdown' to stop\n");
					send(clientfd,buffer,strlen(buffer),0);

					
					strcpy(buffer,"SERVER> ");
					strcat(buffer,connection[clientfd]);
					strcat(buffer," has joined the server\n");

					for( x=serverfd+1; x<max_connect; x++ )
					{
						if( FD_ISSET(x,&main_fd) )
							send(x,buffer,strlen(buffer),0);
					}

					printf("%s",buffer);
				} 

				else
				{
					r = recv(fd,buffer,BUFSIZ,0);
					if( r<1 )
					{
						FD_CLR(fd, &main_fd);		
						strcpy(buffer,"SERVER> ");
						strcat(buffer,connection[fd]);
						strcat(buffer," вышел.\n");

						for( x=serverfd+1; x<max_connect; x++ )
						{
							if( FD_ISSET(x,&main_fd) )
							{
								send(x,buffer,strlen(buffer),0);
							}
						}

						printf("%s",buffer);
					}

					else
					{
						buffer[r] = '\0';			
						if( strcmp(buffer,"shutdown\n")==0 )
						{
							done = true;		
						}
						
						else
						{
	
							strcpy(sendstr,connection[fd]);
							strcat(sendstr,"> ");
							strcat(sendstr,buffer);

							for( x=serverfd+1; x<max_connect; x++ )
							{

								if( FD_ISSET(x,&main_fd) )
								{
									//отправка строки
									send(x,sendstr,strlen(sendstr),0);
								}
							}

							printf("%s",sendstr);
						}	
					}	
				} 
			} 
		} 
	} 
	puts("SERVER> Выход");
	/* закрытие сокера и очистка памяти */
	close(serverfd);
	freeaddrinfo(server);
	return(0);
}
