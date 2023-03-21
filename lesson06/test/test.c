#include "test.h"
#include <stdio.h>

void echo(int a) {
    printf("val1 = %d\n", val1);
    printf("val2 = %d\n", val2);
    printf("%d\n", a);
    val1 = 10;
    val2 = 20;
}