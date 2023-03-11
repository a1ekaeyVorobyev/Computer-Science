#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "stack.c"
#include "cell.h"

//---символы для прорисовки
#define NEWLINE 10
#define SPACE 32

typedef unsigned short bool;
#define true 1
#define false 0

#define TOP_ROW 0
#define BOT_ROW (rowMAX - 1)
#define FAR_LEFT 0
#define FAR_RIGHT (colMAX - 1)

#define BOT_WALL 0
#define RIGHT_WALL 1

//-- размер для лабиринта
static int rowMAX;
static int colMAX;

//иницилизация ячейки
void initСells(cellptr maze);
//распечатоть
void printMaze(cellptr maze);
//гератор
void generatorMaze(cellptr maze);
//генератор куда идти
int getRand();

int main(int argc, char *argv[]) 
{
    srand(time(0));

    if (argc == 1) 
    {    
        colMAX = rowMAX = 15;
    } else if (argc == 2)
        colMAX = rowMAX = (atoi(argv[1]));
    else{
        colMAX = (atoi(argv[1]));
        rowMAX = (atoi(argv[2]));
    }

    cell maze[rowMAX][colMAX];

    initСells(*maze);
    generatorMaze(*maze);
    printMaze(*maze);
    return 0;
}


void generatorMaze(cellptr maze) {
    cellptr start = maze;   
    push(start);

    //так как определенны ниже
    bool allVisited(cellptr cell);
    int getRand(int min, int max);

    //пока стэк не пустой
    while (sp > 0) 
    {
        cellptr current = pop();

        // check that there are unvisited neighbors
        if (!allVisited(current)) 
        {
            push(current);

            cellptr neighbor;
            int dir = 0;

            // get random neighbor that isnt NULL and isnt visited already
            while ((neighbor = current->neighbors[dir = getRand(0, 3)]) == NULL || neighbor->visited)
                    ;
            
            // each cell only has a right wall and a bottom wall
            // so to modify for example the left wall of the current cell
            // you would modify the right wall of the cell left to the current cell


            if (dir == LEFT) {
                neighbor->walls[RIGHT_WALL] = false;            
            }
            if (dir == RIGHT) {
                current->walls[RIGHT_WALL] = false;
            }
            if (dir == BOT) {
                current->walls[BOT_WALL] = false;
            }
            if (dir == TOP) {
                neighbor->walls[BOT_WALL] = false;
            }
        
            neighbor->visited = true;
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
    //for (int i = 0; i < (colMAX * 2); ++i) putchar('_');
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

                // top row has no cells above them
                colptr->neighbors[TOP] = NULL;                          
            } else colptr->neighbors[TOP] = &(rowptr - rowMAX)[col];

            if (row == BOT_ROW) {

                // bottom row has no cells below them
                colptr->neighbors[BOT] = NULL;
            } else colptr->neighbors[BOT] = &(rowptr + rowMAX)[col];

            if (col == FAR_LEFT) {

                // left column has no cells left to them
                colptr->neighbors[LEFT] = NULL;
            } else colptr->neighbors[LEFT] = (colptr - 1);

            if (col == FAR_RIGHT) {

                // right column has no cells right to the,
                colptr->neighbors[RIGHT] = NULL;
            } else colptr->neighbors[RIGHT] = (colptr + 1);
            
            // set all walls to true at the start
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
    if (!isNull(cell->neighbors[BOT])) {
        b = cell->neighbors[BOT]->visited;
    }
    return (l && r && t && b);
}

int getRand(int min, int max){ 
    return (rand() % (max - min + 1) + min);
}
