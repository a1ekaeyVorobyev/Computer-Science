#ifndef STACK
#define STACK

#include "cell.h"

static cellptr cellstack[10000];
static int sp;

static cellptr cellstack[10000];
static int sp;

void push(cellptr cell);
cellptr pop();

#endif