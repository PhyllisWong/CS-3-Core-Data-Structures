#!python

from pprint import pprint
from hashtable import HashTable

class Set(object):

    def __init__(self, elements=None):
        '''Initialize a new empty set structure, and add each element if a sequence is given.'''
        self.size = 0  # Number of entries

        if elements is None:
            # Hashtable initializes with 8 buckets if elements=None
            self.data = HashTable()
        else:
            self.data = HashTable(len(elements))

    def __repr__(self):
        '''Return a string representation of this hash table.'''
        return 'HashTable({!r})'.format(self.data.items())

    def contains(self, element):
        '''Return a boolean indicating whether element is in this set.'''
        '''Use the method from hashtable class to test if contains.'''
        contain = self.data.contains(element)
        return contain

    def add(self, element):
        '''Add element to this set, if not present already.'''
        # Use hashtable set func, takes a key, value pair
        if element not in self.data.keys():
            self.data.set(element, None)
            self.size += 1

    def remove(self, element):
        '''Remove element from this set, if present, or else raise KeyError.'''
        # Detel function raises the value error if not found
        self.data.delete(element)

    def union(self, other_set):
        '''Return a new set that is the union of this set and other_set.'''
        new_set = Set(self.data.keys())

        for element in other_set.data.keys():
            if not self.data.contains(element):
                new_set.add(element)

        return new_set

    def intersection(self, other_set):
        '''Return a new set that is the intersection of this set and other_set.'''
        # Iterate through other_set, at each element, call self.contains, if true, add to new set.
        # Return new set.
        if other_set.data and self.data is not None:
            new_set = Set()

            for element in other_set.data.keys():
                if self.data.contains(element):
                    new_set.add(element)
            return new_set
        else:
            return ValueError('Set is empty')

    def difference(self, other_set):
        '''Return a new set that is the difference of this set and other_set.'''
        if other_set.data and self.data is not None:
            new_set = Set()

            for element in other_set.data.keys():
                if not self.data.contains(element):
                    new_set.add(element)
            return new_set
        else:
            return ValueError('Set is empty')


    def is_subset(self, other_set):
        '''Return a boolean indicating whether other_set is a subset of this set.'''
        if other_set.data and self.data is not None:
            new_set = Set()

            for element in other_set.data.keys():
                if not self.data.contains(element):
                    return False
            return True
        else:
            return ValueError('Set is empty')


def test_set():
	new_set = Set()
	new_set.add("hello 2Day")
	new_set.add("foo")
	new_set.add("bar")
	new_set.add("settlers of catan")
	new_set.contains("foo")
	other_set = Set()
	other_set.add("magic")
	other_set.add("the")
	other_set.add("gathering")
	other_set.add("ouch")
	other_set.add("my")
	other_set.add("brain")
	sets = new_set.union(other_set)
	inter_set = new_set.intersection(other_set)
	print(inter_set.data)
	print(new_set.data)
	print(sets.data)

	print(new_set.contains("foo"))
	print(new_set.contains("bar"))
	print(new_set.data)
	new_set.remove("foo")
	print(new_set.data)
	print(new_set)

if __name__ == '__main__':
	test_set()
