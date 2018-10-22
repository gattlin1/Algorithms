#!/usr/bin/env python3
"""
author: Gattlin Walker
class: CSC 325 - Algorithms
instructor: Anthony Clark
"""

"""
@param1: list of the adjacency matrix for who the person is friends with
@return: number of groups from the adjacency matrix
Sets every person to unexplored (false). Then iterates through every person to 
find who they are friends with (by calling dfs).
"""
def count_friend_circles(friends):
    explored = [False]
    groups = 0

    for i in range(1, len(friends[0])): #start at 1 since we initialized with 0 value
        explored.append(False) #each index corresponds with one person.

    for i in range(len(explored)):
        if not explored[i]:
            groups += 1
            dfs(friends, explored, i)
    return groups

"""
@param1: adjacency matrix list
@param2: array of if the person has been explored or not. The index value 
corresponds with the person. ex. index 0 represents person 1. etc...
@param3: starting index
Searches the adjacency matrix to see if the starting person has any friends.
If they do then explore that friend to see if they have any other friends.
"""
def dfs(friends, explored, start):
    explored[start] = True #sets the person to explored
    for i in range(len(friends[start])):
        if friends[start][i] == 'Y' and not explored[i]:
            dfs(friends, explored, i)

if __name__ == '__main__':
    matrix_filename = input('Please provide a filename containing a friends matrix:\n')

    with open(matrix_filename, 'r') as matrix_file:
        friends = [line.strip() for line in matrix_file.readlines()]
    num_circles = count_friend_circles(friends)
print(f'Number of friend circles: {num_circles}')
