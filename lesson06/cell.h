#include<stdbool.h>

#ifndef CELL
#define CELL

#define LEFT 0
#define RIGHT 1
#define TOP 2 
#define BOTTON 3

typedef struct cellstruct* cellptr; //указатель на сткуктуру ячейки

struct cellstruct{
    cellptr neighbors[4];
    int walls[2];              // [0] = верхнея стена, [1] = правая стена
    bool visited;              // посещали или нет ячейку
};

typedef struct cellstruct cell;

#endif