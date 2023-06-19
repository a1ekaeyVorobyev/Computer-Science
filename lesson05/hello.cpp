/* hello.c */
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string>

using namespace std;

bool isDigit(string text){
	for(int i=0;i<text.length();i++){
		if (text[i]<48 || text[i]>57)
			return false;
	}
	return true;
}

int main (void)
{
	//srand(time(0));
	int a,cnt,seachNumber;
	string text;
	cnt = 5;
	srand(unsigned(time(0)));
	seachNumber = rand()%100;
	//printf ("Загадали число:|%d|\n",10);
	printf ("Загадали число:|%d|\n",seachNumber);
	printf ("Угодайте число от 0 до 100\n");
	while (cnt>0)
	{
		printf ("Введите ваше число\n");
		//scanf("%d", &a); // ввод  переменной a с клавиатуры
		cin>>text;
		if (isDigit(text)){
				a = stoi(text);
				if (seachNumber==a){
					printf ("Вы угадали число\n");
					break;
				}
				if (seachNumber>a){
                        printf ("Больше.\n");
                	}
				if (seachNumber<a){
                        printf ("Меньше.\n");
                	}
				cnt--;
		}
		else {
			printf ("Вводите только числа\n");
			continue;
		}
	}
	if (seachNumber!=a)
		 printf("У вас закончились попытки. Попробуйте еще раз.\n");
}
