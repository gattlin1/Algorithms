Friend Circles Problem

There are n

students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature, i.e., if A is a friend of B and B is a friend of C, then A is also a friend of C.

A friend circle is a group of students who are directly or indirectly friends. Indirect friendships can require multiple levels of indirection.

Your program will take a filename as user input. Your program will print the number of friend circles found in the class.

The input file contains an n
by n matrix containing the characters Y and N. A Y found in the ith row and jth column indicates that studenti and studentj

are friends; an N indicates they are not friends.

You can assume the following:

    Each element of input file will be Y or N
    The number of rows and columns in the input file will be equal
    All students are friends with themselves (the diagonal of the matrix is filled with Ys)
    If studenti

is friends with studentj, then studentj is friends with studenti