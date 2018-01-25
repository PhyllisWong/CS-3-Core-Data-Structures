#!python

from pprint import pprint


class Set(object):

    def __init__(self, elements=None):
        '''initialize a new empty set structure, and add each element if a sequence is given.'''
        self.size = 0  # Number of entries

        if elements is None:
            # Hashtable initializes with 8 buckets if elements=None
            self.data = HashTable()
        else:
            self.data(HashTable(len(elements)))

    def __str__(self):
        '''Return a formatted string representation of this hash table.
        {!r} chooses repr() to format the value passed in.'''
        items = ['{!r}'.format(item) for item in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        '''Return a string representation of this hash table.'''
        return 'HashTable({!r})'.format(self.items())

    def contains(self, element):
        '''Return a boolean indicating whether element is in this set.'''
        '''Use the method from hashtable class to test if contains.'''
        contain = self.data.contains(element)
        return contain

    def add(self, element):
        '''Add element to this set, if not present already.'''
        # Use hashtable set func, takes a key, value pair
        self.data.set(element, None)

    def remove(self, element):
        '''Remove element from this set, if present, or else raise KeyError.'''
        self.data.delete(element)

    def union(self, other_set):
        '''Return a new set that is the union of this set and other_set.'''
        pass

    def intersection(self, other_set):
        '''Return a new set that is the intersection of this set and other_set.'''
        pass

    def difference(self, other_set):
        '''Return a new set that is the difference of this set and other_set.'''
        pass

    def is_subset(self, other_set):
        '''Return a boolean indicating whether other_set is a subset of this set.'''
        pass
