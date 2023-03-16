#include"maze.h"
#include"maze.c"
#include <time.h>
#include <stdio.h>



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