import unittest
from bst import *

def comes_before(a, b):
    return a < b

class BSTIteratorTests(unittest.TestCase):

    def test_prefix(self):
        node = Node(2, Node(1, None, None), Node(3, None, None))
        bst = BinarySearchTree(comes_before)
        bst.node = node
        iterator = prefix_iterator(bst)
        self.assertEqual(next(iterator), 2)
        self.assertEqual(next(iterator), 1)
        self.assertEqual(next(iterator), 3)

        with self.assertRaises(StopIteration):
            next(iterator)

    def test_infix(self):
        node = Node(2, Node(1, None, None), Node(3, None, None))
        bst = BinarySearchTree(comes_before)
        bst.node = node
        iterator = infix_iterator(bst)
        self.assertEqual(next(iterator), 1)
        self.assertEqual(next(iterator), 2)
        self.assertEqual(next(iterator), 3)

        with self.assertRaises(StopIteration):
            next(iterator)

    def test_postfix(self):
        node = Node(2, Node(1, None, None), Node(3, None, None))
        bst = BinarySearchTree(comes_before)
        bst.node = node
        iterator = postfix_iterator(bst)
        self.assertEqual(next(iterator), 1)
        self.assertEqual(next(iterator), 3)
        self.assertEqual(next(iterator), 2)

        with self.assertRaises(StopIteration):
            next(iterator)

if __name__ == '__main__':
    unittest.main()