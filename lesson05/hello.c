/* hello.c */
#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main (void)
{
	//srand(time(0));
	int a,cnt,seachNumber;
	cnt = 5;
	srand(unsigned(time(0)));
	seachNumber = rand()%100;
	//printf ("Загадали число:|%d|\n",10);
	printf ("Загадали число:|%d|\n",seachNumber);
	printf ("Угодайте число от 0 до 100\n");
	while (cnt>0)
	{
		printf ("Введите ваше число\n");
		scanf("%d", &a); // ввод  переменной a с клавиатуры
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
}
