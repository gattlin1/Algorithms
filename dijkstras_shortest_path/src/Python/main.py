#!/usr/bin/env python3
import math
"""
author: Gattlin Walker
email: gattlin1@live.missouristate.edu
class: CSC 325 - Algorithms
instructor: Anthony Clark
"""

"""
@param:  an dictionary of int key value for the node value and an int tuple
         value pair corresponding to the (node, edge) values
@return: the shortest path lengths from the user entered starting node.
"""
def dijkstras(data_set):
    starting_vertex = int(input("Please provide a start vertex label (1..n):\n"))
    path_lengths = [math.inf for values in range(len(data_set))]
    visited = {} 
    visited[starting_vertex] = None
    path_lengths[starting_vertex - 1] = 0
    while len(visited) < len(data_set):
        next_node = -1
        next_shortest_path = math.inf
        for node in list(visited):
            for edge in data_set[node]:
                if edge[0] not in visited and path_lengths[node - 1] + edge[1] < next_shortest_path:
                    next_node = edge[0]
                    next_shortest_path = path_lengths[node - 1] + edge[1]
        visited[next_node] = None
        path_lengths[next_node - 1] = next_shortest_path
    return path_lengths

if __name__ == '__main__':
    data_set = {}
    filename = input('Please provide a filename containing an adjacency list:\n')
    with open(filename, 'r') as file:
        graph = [line.strip() for line in file.readlines()]

    #iterates through each node in the graph and then stores the numbers that
    #it finds into tuple_values.
    for node in graph:
        tuple_values = [] #the first value will always be the node for the data_set
        i = 0

        #whenever there is a digit at the i'th character, create a temporary variable to
        #store that full number. then store it to an array as an integer.
        while i < len(node):
            if node[i].isdigit():
                temp_value = ''
                while i < len(node) and node[i].isdigit():
                    temp_value += node[i]
                    i += 1
                tuple_values.append(int(temp_value))
            else:
                i += 1

        #add the data to the data_set as a tuple (node, edge) values
        data_set[tuple_values[0]] = [(tuple_values[j - 1], tuple_values[j]) for j in range(2, len(tuple_values), 2)]

    distance_from_start = dijkstras(data_set)

    #converts the array into a string of values separated by a ','
    values = ''
    for i in range(len(distance_from_start) - 1):
        values += str(distance_from_start[i]) + ','
    values += str(distance_from_start[len(distance_from_start) - 1])

    print(values)
