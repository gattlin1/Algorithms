#!/usr/bin/env python3
"""
author: Gattlin Walker
class: CSC 325 - Algorithms
instructor: Anthony Clark
"""

"""
@param1: list of the adjacency matrix for who the person is friends with
@return: number of groups from the adjacency matrix
Sets every person to unexplored. Then iterates through every person to 
find who they are friends with (by calling dfs).
"""
def count_friend_circles(friends):
    friends_dict = {0: 'unexplored'}
    groups = 0

    for i in range(1, len(friends[0])): #start at 1 since we initialized with 0 value
        friends_dict[i] = 'unexplored'

    for person in friends_dict:
        if friends_dict[person] == 'unexplored':
            groups += 1
            dfs(friends, friends_dict, person)
    return groups

"""
@param1: adjacency matrix list
@param2: dictionary for if the person (node) has beenn explored
@param3: starting person (node)
Searches the adjacency matrix to see if the starting person has any friends.
If they do then explore that friend to see if they have any other friends.
"""
def dfs(friends, friends_dict, start):
    friends_dict[start] = 'explored' #sets the person to explored
    for i in range(len(friends[start])):
        if friends[start][i] == 'Y' and friends_dict[i] != 'explored':
            dfs(friends, friends_dict, i)

if __name__ == '__main__':
    matrix_filename = input('Please provide a filename containing a friends matrix:\n')

    with open(matrix_filename, 'r') as matrix_file:
        friends = [line.strip() for line in matrix_file.readlines()]
    num_circles = count_friend_circles(friends)
print(f'Number of friend circles: {num_circles}')
