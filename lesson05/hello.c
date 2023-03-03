#include "stdio.h"
#include <stdlib.h>  // чтобы пользоваться функцией rand
#include <time.h> 
#include <string.h>

#define cnt 10 //количество попыток
#define INPUT_BUF_SIZE 256

int isDigit(char* text){
    int i=0;
    char c;
    while(i<INPUT_BUF_SIZE)
    {
        c = text[i];
        if (c == 10){
            return 0;
        }else if (c < 48 || c > 57)
            return 1;
        i++;
    }
    return 0;
}

int main()
{
    srand(time(NULL));
    int seachNumber = rand()%100;
    //printf("%d ", seachNumber);
    int i=0;
    int val = 0;
    char buf[INPUT_BUF_SIZE];
    while( i< cnt ){
        printf("Введите ваше число\n");
        //scanf("%c", &a);
        fgets(buf, INPUT_BUF_SIZE, stdin);
        if (isDigit(buf))
        {
            printf("Надо вводить только символы.\n");
        }else{
            val = atoi(buf);
            if (seachNumber == val){
                printf ("Вы угадали число\n");
                break;
            }
            if (seachNumber < val){
                printf ("Больше.\n");
            }
            if (seachNumber > val){
                printf ("Меньше.\n");
            }
            i++;
        }
    }
    if (seachNumber != val)
        printf("У вас закончились попытки. Попробуйте еще раз.\n");
	return 0;
}