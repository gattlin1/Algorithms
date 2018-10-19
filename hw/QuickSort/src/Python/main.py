#!/usr/bin/env python3
"""
This program is used to showcase the performance speeds of different quicksort variants
Quick Sort First: always takes the first element in the array and then partitions it.
Quick Sort Median3: takes the median value of the first, middle and last value.
Quick Sort Random: takes a random index value in the left and right bound as the pivot
"""
import random #for the random integer in quickSort random
COUNT = 0 #a global variable for counting the work done in quicksort

"""
@param1: An array we are trying to sort
@param2: the left bound of the array/subarray
@param3: the right bound of the array/subarray
Param2 and Param3 vary depending on which recursive call we are in
these are the bounds of the varying amount of numbers we are trying to sort
@return: returns the pivot index
"""
def partition(A, left_index, right_index):
    pivot = A[left_index]
    i = left_index + 1
    global COUNT
    for j in range(left_index + 1, right_index):
        if A[j] < pivot:
            A[j], A[i] = A[i], A[j] #swap
            i += 1
    A[left_index], A[i - 1] = A[i - 1], A[left_index] #put the pivot in the correct place
    COUNT += right_index - left_index - 1 #increments for how many times the pivot was tested
    return i - 1

#Quick Sort Variant where we take the first element as are pivot
def quick_sort_first(A, left, right):
    if left < right:
        pivot_index = partition(A, left, right)
        quick_sort_first(A, left, pivot_index) #quick sort left recursive call
        quick_sort_first(A, pivot_index + 1, right) #quick sort right recursive call

#Quick Sort Variant where we take a random element as are pivot
def quick_sort_random(A, left, right):
    if left < right:
        pivot = random.randint(left, right - 1)
        A[pivot], A[left] = A[left], A[pivot]
        pivot_index = partition(A, left, right)
        quick_sort_random(A, left, pivot_index) #quick sort left recursive call
        quick_sort_random(A, pivot_index + 1, right) #quick sort right recursive call

#Quick Sort Variant where we take the median of the first, middle and last elements as are pivot
def quick_sort_median3(A, left, right):
    if left < right:
        get_median(A, left, right - 1)
        pivot_index = partition(A, left, right) #sorts the pivotIndex into the correct position
        quick_sort_median3(A, left, pivot_index) #quick sort left recursive call
        quick_sort_median3(A, pivot_index + 1, right) #quick sort right recursive call

#Helper function to get the median value and then swap it into the left most position
#at a given recursive call
def get_median(A, left, right):
    if right - left <= 1: #if there are only two variables we are testing
        if A[left] > A[right]:
            A[left], A[right] = A[right], A[left]
    else:
        #values for the first, middle and last indexes.
        first = A[left]
        middle = A[left + ((right - left) // 2)]
        last = A[right]

        #NOTE: We do not do anything if the first index is the middle value because
        #it is already in the left most index

        #if statement for if the middle or last value is the median value of first, middle,
        #and last. Depending on which one is the median we swap its value with the first value
        if middle > first and middle < last or middle < first and middle > last:
            A[left + ((right - left) // 2)], A[left] = first, middle
        elif last > first and last < middle or last < first and last > middle:
            A[right], A[left] = first, last

def main():
    #prompts for the user for the filename and quick sort variant
    file_name = input("Please enter a filename:\n")
    quick_sort_variant = input("Please enter a Quicksort variant:\n")

    #opens and reads the file
    file = open(file_name, 'r')

    #appends the stripped values to the array arr
    arr = []
    for i in file:
        arr.append(int(i.strip()))

    #elif statements for each of the quick sort variants
    #NOTE: we start the left at 1 because the first number
    #denotes the number of elements in the the text file
    if quick_sort_variant == "first":
        quick_sort_first(arr, 1, len(arr))
    elif quick_sort_variant == "random":
        quick_sort_random(arr, 1, len(arr))
    elif quick_sort_variant == "median3":
        quick_sort_median3(arr, 1, len(arr))

    print(COUNT) #prints the count


main()
