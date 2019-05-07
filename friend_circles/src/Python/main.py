#!/usr/bin/env python3
"""
author: Gattlin Walker
email: gattlin1@live.missouristate.edu
"""

def dfs(friends, explored, start):
    explored[start] = True
    for i in range(len(friends[start])):
        if friends[start][i] == 'Y' and not explored[i]:
            dfs(friends, explored, i)

def count_friend_circles(friends):
    explored = [False]
    groups = 0

    for i in range(1, len(friends[0])):
        explored.append(False)

    for i in range(len(explored)):
        if not explored[i]:
            groups += 1
            dfs(friends, explored, i)
    return groups

if __name__ == '__main__':
    matrix_filename = input('Please provide a filename containing a friends matrix:\n')

    with open(matrix_filename, 'r') as matrix_file:
        friends = [line.strip() for line in matrix_file.readlines()]
    num_circles = count_friend_circles(friends)
    print(f'Number of friend circles: {num_circles}')
