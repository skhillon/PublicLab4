import unittest
from linked_list import *

class ObjectIteratorTests(unittest.TestCase):
    lst1 = None
    lst2 = Pair(1, None)
    lst3 = Pair(4, Pair(3, Pair(2, Pair(1, None))))
    obj1 = object_iterator(lst1)
    obj2 = object_iterator(lst2)
    obj3 = object_iterator(lst3)

    def test_repr(self):
        self.assertEqual(repr(self.obj1), "Iterator(None)")

    def test_object_iterator(self):
        self.assertEqual(object_iterator(None), self.obj1)

    def test_has_next(self):
        self.assertFalse(has_next(self.obj1))
        self.assertTrue(has_next(self.obj2))

    def test_next_obj2(self):
        self.assertEqual(next(self.obj2), 1)

    def test_next_obj3(self):
        self.assertEqual(next(self.obj3), 4)
        self.assertEqual(next(self.obj3), 3)
        self.assertEqual(next(self.obj3), 2)
        self.assertEqual(next(self.obj3), 1)

        with self.assertRaises(StopIteration):
            next(self.obj3)

if __name__ == '__main__':
    unittest.main()