#ifndef STACK
#define STACK

#include "cell.h"
#include "null.h"

void push(cellptr cell);
cellptr pop();
int getSP();

#endif