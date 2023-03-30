#!/usr/bin/python3
"""
function that finds a peak in a list of unsorted
integers
"""


def divide(array, low, high):
    """divide and conquer"""

    mid = int((high + low)/2)
    if array[mid-1] <= array[mid] >= array[mid+1]:
        return array[mid]
    elif array[mid] > array[mid+1]:
        return divide(array, low, mid-1)
    elif array[mid] < array[mid+1]:
        return divide(array, mid+1, high)


def find_peak(list_of_integers):
    """Find peak of a list"""

    if not list_of_integers:
        return None
    return divide(list_of_integers, 0, len(list_of_integers)-1)
