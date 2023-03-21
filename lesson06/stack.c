#include "stack.h"
#include <stdio.h>

cellptr cellstack[1000];
int sp = 0;

void push(cellptr cell) 
{
    cellstack[sp++] = cell;
}

cellptr pop() 
{
    return (sp > 0) ? cellstack[--sp] : NULL;
}

int getSP()
{
    return sp;
}