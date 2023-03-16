#include "stack.h"

void push(cellptr cell) 
{
    cellstack[sp++] = cell;   
}

cellptr pop() 
{
    return (sp > 0) ? cellstack[--sp] : NULL;
}