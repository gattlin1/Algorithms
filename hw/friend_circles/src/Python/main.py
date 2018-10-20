#!/usr/bin/env python3
"""
author: Gattlin Walker
class: CSC 325 - Algorithms
instructor: Anthony Clark
"""

"""
@param1: list of the adjacency matrix for who the person is friends with
@return: number of groups from the adjacency matrix
"""
def count_friend_circles(friends):
    #initializes the dictionary and sets the first value to unexplored
    friends_dict = {0: 'unexplored'}

    #gives every person (node) the value 'unexplored'
    for i in range(len(friends[0])):
        friends_dict[i] = 'unexplored'
    
    #initialized the groups value to 0. This will be used to return the number of groups in the end
    groups = 0
    
    #iterates through all of the people in the friends dictionary
    #if the person is unexplored then that is starting a new group 
    #because dfs will find the whole group when called.
    for person in friends_dict:
        if friends_dict[person] == 'unexplored':
            groups += 1
            dfs(friends, friends_dict, person)
    return groups

"""
@param1: adjacency matrix list
@param2: dictionary 
@param3: start position
Searches the adjacency matrix to see if the starting person has any friends.
If they do then explore that friend to see if they have any other friends.
"""
def dfs(friends, friends_dict, start):
    friends_dict[start] = 'explored' #sets the person to explored 
    for i in range(len(friends[start])):
        #if they are friends and the person hasn't already been explored then check if that person
        #has any more friends.
        if friends[start][i] == 'Y' and friends_dict[i] != 'explored':
            dfs(friends, friends_dict, i)

if __name__ == '__main__':

    matrix_filename = input('Please provide the name of a file that contains a friends matrix:\n')

    with open(matrix_filename, 'r') as matrix_file:
        friends = [line.strip() for line in matrix_file.readlines()]
    num_circles = count_friend_circles(friends)
    print(f'Number of friend circles: {num_circles}')