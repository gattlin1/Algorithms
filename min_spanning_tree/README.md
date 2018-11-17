Minimum Spanning Trees
Your program will prompt users for a filename and a start vertex label, and then it will output the cost of the minimum spanning tree.

The input file
Your programs will read a file, the name of which will be provided via a command line argument. The file will include all of the information needed to create an undirected graph with edge costs. The file has the following format:

[n] [m]
[v_i] [v_j] [c1]
[v_a] [v_b] [c2]
Where the first line gives values for n and m, which are the number of vertices and number of edges, respectively. Each line after the first gives two vertex numbers (v_i and v_j; v_a and v_b) and then a cost for that edge (cx). Here is an example input file (it is also attached):

5 7
1 2 2
1 4 6
2 3 3
2 4 8
2 5 5
3 5 7
4 5 9
