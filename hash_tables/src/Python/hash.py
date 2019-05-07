#!/usr/bin/env python3

def djb2(arr):
    hashed_array = []
    magic = 33
    for s in arr:
        hash = 5381
        for c in s:
            hash = hash * magic + ord(c)
        hashed_array.append(hash & 0xFFFFFFFF)
    return hashed_array

if __name__ == "__main__":
    letters = ['D', 'H', 'L', 'P']
    unicode_values = [ord(char) for char in letters]
    for value in unicode_values:
        print("Unicode: ", value, "  Mod 4: ", value % 4)

    for value in djb2(['Hello there!', 'CSC 325', 'Algorithms', 'Data Structures']):
        print("Hash: ", value, "Bucket: ", value % 10)

