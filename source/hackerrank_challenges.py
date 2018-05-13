import sys
import binarytree as b


def check(node, min, max):
    print('min: {}, max: {}'.format(min, max))
    if node == None:
        return True
    if node.data <= min or node.data >= max:
        return False
    return check(node.left, min, node.data) and check(node.right, node.data, max)


def check_binary_search_tree_(node):
        return check(node, float('-inf'), float('inf'))


def test_binary_search_tree():
    items = [1, 2, 3, 4, 5, 6, 7]
    tree = b.BinarySearchTree(items)

    for item in items:
        tree.insert(item)

    check_binary_search_tree_(node)


if __name__ == '__main__':
      # main()
    test_binary_search_tree()
