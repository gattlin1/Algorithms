#!/usr/bin/env python3
import math
"""
author: Gattlin Walker
email: gattlin1@live.missouristate.edu
class: CSC 325 - Algorithms
instructor: Anthony Clark
"""

def dijkstras(data_set):
    starting_vertex = int(input("Please provide a start vertex label (1..n):\n"))
    path_lengths = [math.inf for values in range(len(data_set))]
    visited = {starting_vertex} 
    path_lengths[starting_vertex - 1] = 0
    while len(visited) < len(data_set):
        next_node = -1
        next_shortest_path = math.inf
        for node in list(visited):
            for edge in data_set[node]:
                if edge[0] not in visited and path_lengths[node - 1] + edge[1] < next_shortest_path:
                    next_node = edge[0]
                    next_shortest_path = path_lengths[node - 1] + edge[1]
        visited.add(next_node)
        path_lengths[next_node - 1] = next_shortest_path
    return path_lengths

def add_edge(G, node, connecting_node, edge):
    if node in G:
        G[node].append((connecting_node, edge))
    else:
        G[node] = [(connecting_node, edge)]

if __name__ == '__main__':
    data_set = {}
    filename = input('Please provide a filename containing an adjacency list:\n')
    with open(filename, 'r') as file:
        for line in file:
            values = line.split()
            starting_node = int(values[0])
            for v in values[1:]:
                connecting_node, edge = tuple(int(x) for x in v.split(','))
                add_edge(data_set, starting_node, connecting_node, edge)

    distance_from_start = dijkstras(data_set)

    print(distance_from_start)
