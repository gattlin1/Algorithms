Dijkstra's Shortest Path Algorithm
------------------------------------
Your program will prompt users for a filename and a start vertex number and it will output the shortest path from the start vertex to all other vertices.

Input File
------------
The file will include all of the information needed to create a directed graph (I decided to go with a directed graph as it is slightly easier to code).

The format of this file is referred to as an adjacency list. Here is an example of such a file:

1 2,1 8,2
2 1,1 3,1
3 2,1 4,1
4 3,1 5,1
5 4,1 6,1
6 5,1 7,1
7 6,1 8,1
8 7,1 1,2
Each line of the file contains the following information: a vertex identifier (a value from 1 to n) and then a list of edge information where each edge contains a pair of values (the connecting vertex and an integer value for the edge length).

For example, on the third line above (3 2,1 4,1) we can see that vertex 3 is connected to vertex 2 with a length of 1, and vertex 3 is also connected to vertex 4 with a length of 1.