#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    # enumerate returns the index and the value at the index
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests

    # not found base case
    if index > len(array) -1:
        return None

    # found base case
    if array[index] == item:
        return index

    return linear_search_recursive(array, item, (index + 1))


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    array = sorted(array)
    # set the index at the middle of the list
    index = int((len(array)-1)/2)

    # if the first index place matches what we are looking for, return the position
    if array[index] == item:
        return index

    # if the list is empty, return none
    if len(array) == 0:
        return None

    # as long as the item at the index does not match the serach item, check if
    # the item is bigger than or smaller than the item at the index
    while array[index] != item:
        if item > array[index]:
            # reset array to the right side of the index to the end
            array = array[index:]
            index = int((len(array)-1)/2)
        else:
            # reset array to the left side of the index from the beginning
            array = array[:index]
            index = int((len(array)-1)/2)
        return None
    return index


def binary_search_recursive(array, item, left=None, right=None):
    array = sorted(array)

    # set the left and the right positions to find the middle
    if right is None:
         right = len(array) -1
    if left is None:
        left = 0

    mid = int((right + left)//2)


    # Return item position if it is located at the middle
    if array[mid] == item:
        return mid
     # If item is less than the item at the current positition, move search area to the left
    elif array[mid] < item:
        return binary_search_recursive(array, item, mid+1, right)
     # If item is greater than the item at the current positition, move search area to the right
    else:
        return binary_search_recursive(array, item, left, mid-1)


if __name__ == '__main__':
    names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']
    # linear_search(names, 'Jeremy')
    print(binary_search_recursive(names, 'Jeremy'))
