#include"maze.h"
#include"stack.h"
//#include"stack.c"
#include <time.h>
#include <stdio.h>
#include "null.h"


void initMaze(int row,int col){
    rowMAX = row;
    colMAX = col;
}

void generatorMaze(cellptr maze) {
    srand(time(0));
    cellptr start = maze;   
    push(start);

    //так как определенны ниже
    bool allVisited(cellptr cell);
    int getRand(int min, int max);

    int i=0;
    //пока стэк не пустой
    while (getSP() > 0) 
    {
        cellptr current = pop();

        if (!allVisited(current)) 
        {
            push(current);

            cellptr neighbor;
            int dir = 0;

            while ((neighbor = current->neighbors[dir = getRand(0, 3)]) == NULL || neighbor->visited)
            {
               
            }
            
            switch(dir) 
            {
                case LEFT:
                    neighbor->walls[RIGHT_WALL] = false;    
                break;
                case RIGHT:
                    current->walls[RIGHT_WALL] = false;
                break;
                case BOTTON:
                    current->walls[BOT_WALL] = false;
                break;
                case TOP:
                    neighbor->walls[BOT_WALL] = false;
                break;
            }
            
            neighbor->visited = true;
            i++;
            push(neighbor);         
        }       
    }
}

void printMaze(cellptr maze)
 {
    system("clear");
  
    cellptr cptr = maze;

    // распечаиываем верхнюб часть лабиринта
    for (int i = 0; i < (colMAX * 2); ++i) putchar('_');
    putchar(NEWLINE);
    //распечаиываем лабиринт 
    for (int i = 0; i < (colMAX * rowMAX); ++i) {

        if (cptr->neighbors[LEFT] == NULL) putchar('|');

       if (cptr->walls[BOT_WALL] != false) {
            putchar('_');
        } else putchar(SPACE);

        if (cptr->walls[RIGHT_WALL] != false) {
            putchar('|');
        } else 
        if (i > (colMAX * rowMAX)-colMAX-1)
            putchar('_'); 
        else
            putchar(SPACE);

        if (cptr->neighbors[RIGHT] == NULL) {
            putchar(NEWLINE);
        }
        cptr++; 
    }
    putchar(NEWLINE);
}

void initСells(cellptr maze) 
{
    cellptr rowptr, colptr;
    int row, col;
    for (row = 0; row < rowMAX; ++row) {
        rowptr = &maze[rowMAX * row];
        colptr = rowptr;

        for (col = 0; col < rowMAX; ++col) {  
            if (row == TOP_ROW) {

                colptr->neighbors[TOP] = NULL;                          
            } else colptr->neighbors[TOP] = &(rowptr - rowMAX)[col];

            if (row == BOT_ROW) {

                colptr->neighbors[BOTTON] = NULL;
            } else colptr->neighbors[BOTTON] = &(rowptr + rowMAX)[col];

            if (col == FAR_LEFT) {

                colptr->neighbors[LEFT] = NULL;
            } else colptr->neighbors[LEFT] = (colptr - 1);

            if (col == FAR_RIGHT) {

                colptr->neighbors[RIGHT] = NULL;
            } else colptr->neighbors[RIGHT] = (colptr + 1);
            
            colptr->walls[BOT_WALL] = true;                 
            colptr->walls[RIGHT_WALL] = true;

            colptr++->visited = false;   
        }  
    } 
}

bool isNull(cellptr cell) 
{
    return cell == NULL;  
}

bool allVisited(cellptr cell) 
{
    int l, r, t, b;
    l = r = t = b = 1;
    if (!isNull(cell->neighbors[LEFT])) {
        l = cell->neighbors[LEFT]->visited;
    }
    if (!isNull(cell->neighbors[RIGHT])) {
        r = cell->neighbors[RIGHT]->visited;
    }
    if (!isNull(cell->neighbors[TOP])) {
        t = cell->neighbors[TOP]->visited;
    }
    if (!isNull(cell->neighbors[BOTTON])) {
        b = cell->neighbors[BOTTON]->visited;
    }
    return (l && r && t && b);
}

int getRand(int min, int max){ 
    return (rand() % (max - min + 1) + min);
}