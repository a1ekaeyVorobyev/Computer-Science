#include"maze.h"

int main(int argc, char *argv[]) 
{
    if (argc == 1) 
    {    
        colMAX = rowMAX = 15;
    } else if (argc == 2)
        colMAX = rowMAX = (atoi(argv[1]));
    else{
        colMAX = (atoi(argv[1]));
        rowMAX = (atoi(argv[2]));
    }
    initMaze(colMAX,rowMAX);
    cell maze[rowMAX][colMAX];
 
    initСells(*maze);
    generatorMaze(*maze);
    printMaze(*maze);
    return 0;
}