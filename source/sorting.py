#!python
from binarytree import BinarySearchTree


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Check that all adjacent items are in order, return early if not
    for i in range(0, len(items)-1):
        if items[i] > items[i+1]:
            return False
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order

    if is_sorted(items) is False:
        # range is exclusive
        for i in range(0, len(items)-1):
            temp = items[i]

            if items[i] > items[i+1]:
                temp = items[i+1]
                items[i+1] = items[i]
                items[i] = temp

        # exit this block and go back to line 23 to check if it is sorted
        bubble_sort(items)


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    for i in range(len(items)):
        # track the current smallest value
        smallest_index = i
        # loop from the current smallest value
        for j in range(i+1,len(items)):
            if items[j] < items[smallest_index]:
                # if new value is less that our smallest value,
                # change smallest value to this
                smallest_index = j
        if smallest_index != i:
            #swap the values
            items[smallest_index], items[i] = items[i], items[smallest_index]



def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    # start loop at second element since the first item is already sorted
    for j in range(1, len(items)):
        # The item we are going to insert into the sorted section of the array
        unsorted_item = items[j]

        # the index we compare with unsorted_item
        i = j-1
        # keep moving the unsorted_item to the left as long as it's smaller than
        # the last item in the sorted array
        #if i == -1 means that this key belongs at the start
        while (i > -1) and unsorted_item < items[i]:
            # move the last object compared one step ahead to make room for unsorted
            items[i+1] = items[i]
            i -= 1
        # i is not greater than unsorted, means unsorted_item belongs at i+1
        items[i+1] = unsorted_item


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    left, right = items1, items2

    if not len(left) or not len(right):
        return right or left

    merged_list = []
    left_index, right_index = 0, 0

    #Assending 
    while (len(merged_list) < len(left) + len(right)):
        if left[left_index] < right[right_index]:
            merged_list.append(left[left_index])
            left_index += 1
        else:
            merged_list.append(right[right_index])
            right_index += 1

        if left_index == len(left) or right_index == len(right):
            merged_list.extend(left[left_index:] or right[right_index:])
            break

    return merged_list


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    # Divide items list into approximately equal halves
    middle = len(items)//2
    left = items[: middle]
    right = items[middle :]

    # Sort each half using any sorting algorithm
    insertion_sort(left)
    insertion_sort(right)

    # Combine sorted halves into one sorted list
    items[:] = merge(left, right)


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Check if list is so small it's already sorted (base case)
    if len(items) < 2:
        return

    # Split items list into approximately equal halves
    middle = len(items)//2
    left = items[: middle]
    right = items[middle :]

    # Sort each half by recursively calling merge sort
    merge_sort(left)
    merge_sort(right)

    # Merge sorted halves into one list in sorted order
    items[:] = merge(left, right)


def tree_sort(items):
    '''Running time best and worst case running time: O(n log n).'''
    tree = BinarySearchTree()

    for i in items:
        tree.insert(i)

    return tree.items_in_order


def quicksort(items):
    """Time complexity: Best case O(n log(n)) is when the pivot is in the exact middle.
     Worst case O(n^2) is when the pivot is either the lowest or the highest value."""
    # set the base case
    if len(items) <=1:
        return

    # collect all values lesser than and greater than the pivot
    lesser = []
    greater = []
    # Set the pivot as the first item in the unsorted list
    pivot = items[0]

    # iterate over the items list
    for i in range(1, len(items)):
        if items[i] < pivot:
            lesser.append(items[i])
        else:
            greater.append(items[i])
    # call the func recursively
    quicksort(lesser)
    quicksort(greater)
    # Concatinate the lists with the pivot in sorted order
    items[:] = lesser + [pivot] + greater



def random_ints(count=20, min=1, max=50):
    """Return a list of `count` integers sampled uniformly at random from
    given range [`min`...`max`] with replacement (duplicates are allowed)."""
    import random
    return [random.randint(min, max) for _ in range(count)]


def test_sorting(sort=bubble_sort, num_items=20, max_value=50):
    """Test sorting algorithms with a small list of random items."""
    # Create a list of items randomly sampled from range [1...max_value]
    items = random_ints(num_items, 1, max_value)
    print('Initial items: {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))

    # Change this sort variable to the sorting algorithm you want to test
    # sort = selection_sort
    print('Sorting items with {}(items)'.format(sort.__name__))
    sort(items)
    print('Sorted items:  {!r}'.format(items))
    print('Sorted order?  {!r}\n'.format(is_sorted(items)))
    return (is_sorted(items))


def main():
    """Read command-line arguments and test sorting algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name

    if len(args) == 0:
        script = sys.argv[0]  # Get script file name
        print('Usage: {} sort num max'.format(script))
        print('Test sorting algorithm `sort` with a list of `num` integers')
        print('    randomly sampled from the range [1...`max`] (inclusive)')
        print('\nExample: {} bubble_sort 10 20'.format(script))
        print('Initial items: [3, 15, 4, 7, 20, 6, 18, 11, 9, 7]')
        print('Sorting items with bubble_sort(items)')
        print('Sorted items:  [3, 4, 6, 7, 7, 9, 11, 15, 18, 20]')
        return

    # Get sort function by name
    if len(args) >= 1:
        sort_name = args[0]
        # Terrible hack abusing globals
        if sort_name in globals():
            sort_function = globals()[sort_name]
        else:
            # Don't explode, just warn user and show list of sorting functions
            print('Sorting function {!r} does not exist'.format(sort_name))
            print('Available sorting functions:')
            for name in globals():
                if name.find('sort') >= 0:
                    print('    {}'.format(name))
            return

    # Get num_items and max_value, but don't explode if input is not an integer
    try:
        num_items = int(args[1]) if len(args) >= 2 else 20
        max_value = int(args[2]) if len(args) >= 3 else 50
        # print('Num items: {}, max value: {}'.format(num_items, max_value))
    except ValueError:
        print('Integer required for `num` and `max` command-line arguments')
        return

    # Test sort function
    test1 = test_sorting(sort_function, num_items, max_value)
    print('Test sorting: {!r}'.format(test1))


if __name__ == '__main__':
    main()
    # print("HERE")
