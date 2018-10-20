#!/usr/bin/env python3

def count_friend_circles(friends):
    return 0

if __name__ == '__main__':

    matrix_filename = input('Please provide the name of a file that contains a friends matrix:\n')

    with open(matrix_filename, 'r') as matrix_file:
        friends = [line.strip() for line in matrix_file.readlines()]

    num_circles = count_friend_circles(friends)
    print(f'Number of friend circles: {num_circles}')