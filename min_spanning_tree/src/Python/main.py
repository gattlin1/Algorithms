#!/usr/bin/env python3
import math
"""
author: Gattlin Walker
email: gattlin1@live.missouristate.edu
class: CSC 325 - Algorithms
instructor: Anthony Clark
"""

"""
@param1: a dictionary containing the node as the key and a list of all 
         the node edge pairs in the form of tuples ex 1: [(2,1), (3,2)] etc...
@param2: a node used to append to the graph
@param3: a node used to append to the graph
@param4: the edge value connecting param2 and param3
helper function to add an edge 
"""
def add_edge(G, v1, v2, ce):
    if v1 in G:
        G[v1].append((v2, ce))
    else:
        G[v1] = [(v2, ce)]
    if v2 in G:
        G[v2].append((v1, ce))
    else:
        G[v2] = [(v1, ce)]

"""
@param1: a dictionary containing the node as the key and a list of all 
         the node edge pairs in the form of tuples ex 1: [(2,1), (3,2)] etc...
@param2: an integer denoting the starting vertex
@return: returns the minimum length to connect all values in the tree
"""
def prims(G, starting_vertex):
    total_length = 0 #will return the minimum length needed to connect all nodes
    connected = {starting_vertex} #nodes that we have already connected

    #while all the nodes are not connected
    while len(connected) < len(G):

        #values used to find the shortest edge value
        shortest_edge = math.inf
        closest_node = -1

        #checks all of the node's edges that are in connected 
        for node in connected:
            for candidate_node, edge_cost in G[node]:
                if edge_cost < shortest_edge and candidate_node not in connected:
                    shortest_edge = edge_cost
                    closest_node = candidate_node
        
        #add the shortest edge value to the total length and add that corresponding
        #node to the connected list.
        total_length += shortest_edge
        connected.add(closest_node)
    return total_length



if __name__ == '__main__':
    input_filename = input('Please provide an input filename:\n')
    input_vertex = int(input('Please provide a start vertex label (1..n):\n'))

    G = {}
    with open(input_filename, 'r') as input_graph_file:
        n, m = tuple(int(x) for x in input_graph_file.readline().split())
        for line in input_graph_file:
            v1, v2, ce = tuple(int(v) for v in line.split())
            add_edge(G, v1, v2, ce)

    print(prims(G, input_vertex))
    