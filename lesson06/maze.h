#include "stack.h"
#include "cell.h"

#include <stdio.h>
#include <stdlib.h>
#include <time.h>


#ifndef MAZE
#define MAZE

#define NEWLINE 10
#define SPACE 32

#define TOP_ROW 0
#define BOT_ROW (rowMAX - 1)
#define FAR_LEFT 0
#define FAR_RIGHT (colMAX - 1)

#define BOT_WALL 0
#define RIGHT_WALL 1

static int rowMAX ;
static int colMAX ;

void initMaze(int row, int col);
//иницилизация ячейки
void initСells(cellptr maze);
//распечатоть
void printMaze(cellptr maze);
//гератор
void generatorMaze(cellptr maze);
//генератор куда идти
int getRand();

bool isNull(cellptr cell);

bool allVisited(cellptr cell);

#endif
