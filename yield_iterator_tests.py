import unittest
from linked_list import yield_iterator, Pair

class YieldIteratorTests(unittest.TestCase):

    def test_yield_iterator_short(self):
        iterator = yield_iterator(Pair(1, None))
        self.assertEqual(next(iterator), 1)

        with self.assertRaises(StopIteration):
            next(iterator)

    def test_yield_iterator_big(self):
        iterator = yield_iterator(Pair(4, Pair(3, Pair(2, Pair(1, None)))))
        self.assertEqual(next(iterator), 4)
        self.assertEqual(next(iterator), 3)
        self.assertEqual(next(iterator), 2)
        self.assertEqual(next(iterator), 1)

        with self.assertRaises(StopIteration):
            next(iterator)

if __name__ == '__main__':
    unittest.main()