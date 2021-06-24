Rat In A Maze 

this repository contains two folder which work 
on the backtracking algorithm 

each folder has 4 python files among which 3
are modules 

MazeMaps: contains 9 different maps of maze
that gives out one out of nine maps each time
its funcion is called.

SolveMaze module:(Using Backtracking Algorithm)
finds the optimal path to reach the end of the
maze given by MazeMaps and gives the string 
output of direction as L for left R for right 
U for up and D for down

BlockageFinder: module finds all the places the
rat (or character) cannot go in the maze given
by the MazeMaps module


Rat In A Maze(or AmongUs Maze): the main file
imports all the modules first MazeMaps gives
a random maze to the the program then SolveMaze
outputs the optimal path to reach the end of 
the maze in the form of string then the main
Rat In A Maze file itrates over the string 
and moves the character using pygame library 
one by one while the blockage detector give 
the coordinates of the point where the 
character cannot move and program places
a blockage image on those coordinates



