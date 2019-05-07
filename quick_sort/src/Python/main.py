#!/usr/bin/env python3
"""

"""
import random
COUNT = 0

def partition(A, left_index, right_index):
    pivot = A[left_index]
    i = left_index + 1
    global COUNT
    for j in range(left_index + 1, right_index):
        if A[j] < pivot:
            A[j], A[i] = A[i], A[j]
            i += 1
    A[left_index], A[i - 1] = A[i - 1], A[left_index]
    COUNT += right_index - left_index - 1 #increments for how many times the pivot was tested
    return i - 1

def quick_sort_first(A, left, right):
    if left < right:
        pivot_index = partition(A, left, right)
        quick_sort_first(A, left, pivot_index)
        quick_sort_first(A, pivot_index + 1, right)

def quick_sort_random(A, left, right):
    if left < right:
        pivot = random.randint(left, right - 1)
        A[pivot], A[left] = A[left], A[pivot]
        pivot_index = partition(A, left, right)
        quick_sort_random(A, left, pivot_index)
        quick_sort_random(A, pivot_index + 1, right)

def quick_sort_median3(A, left, right):
    if left < right:
        get_median(A, left, right - 1)
        pivot_index = partition(A, left, right)
        quick_sort_median3(A, left, pivot_index)
        quick_sort_median3(A, pivot_index + 1, right)

#Helper function to get the median value and then swap it into the left most position
#at a given recursive call
def get_median(A, left, right):
    if right - left <= 1:
        if A[left] > A[right]:
            A[left], A[right] = A[right], A[left]
    else:
        first = A[left]
        middle = A[left + ((right - left) // 2)]
        last = A[right]

        if middle > first and middle < last or middle < first and middle > last:
            A[left + ((right - left) // 2)], A[left] = first, middle
        elif last > first and last < middle or last < first and last > middle:
            A[right], A[left] = first, last

if __name__ == "__main__":
    file_name = input("Please enter a filename:\n")
    quick_sort_variant = input("Please enter a Quicksort variant:\n")

    file = open(file_name, 'r')

    arr = []
    for i in file:
        arr.append(int(i.strip()))

    #NOTE: we start the left at 1 because the first number
    #denotes the number of elements in the the text file
    if quick_sort_variant == "first":
        quick_sort_first(arr, 1, len(arr))
    elif quick_sort_variant == "random":
        quick_sort_random(arr, 1, len(arr))
    elif quick_sort_variant == "median3":
        quick_sort_median3(arr, 1, len(arr))

    print(COUNT)