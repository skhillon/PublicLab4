import unittest
from bst import *

class BSTTestCases(unittest.TestCase):

    bst_node = Node(17, 
                    Node(5, 
                        Node(2, None, None),
                        Node(11, 
                            Node(9, 
                                Node(8, None, None),
                                None),
                            Node(16, None, None)
                            )
                        ),
                    Node(35, 
                        Node(29, None, None),
                        Node(38, None, None)
                        )
                    )

    def test_repr(self):
        def comes_before(a, b):
            return a < b

        tiny_node = Node(12, None, None)
        node_repr = "Node(12, None, None)"

        bst = BinarySearchTree(comes_before)
        bst.node = tiny_node
        bst_repr = "BinarySearchTree(Node(12, None, None))"
        self.assertEqual(repr(tiny_node), node_repr)
        self.assertEqual(repr(bst), bst_repr)

    def test_is_empty(self):
        def comes_before(a, b):
            return a < b

        bst = BinarySearchTree(comes_before)
        bst.node = self.bst_node


        self.assertFalse(is_empty(bst))
        self.assertTrue(is_empty(BinarySearchTree(comes_before)))

    def test_insert(self):
        def comes_before(a, b):
            return a < b

        bst = BinarySearchTree(comes_before)
        bst.node = self.bst_node

        inserted_bst_node = Node(17, 
                                Node(5, 
                                    Node(2, None, None),
                                    Node(11, 
                                        Node(9, 
                                            Node(8, None, None),
                                            None),
                                        Node(16, None, None)
                                        )
                                    ),
                                Node(35, 
                                    Node(29, 
                                        Node(18, None, None), 
                                        None),
                                    Node(38, None, None)
                                    )
                                )

        inserted_bst = BinarySearchTree(comes_before)
        inserted_bst.node = inserted_bst_node

        empty_bst = BinarySearchTree(comes_before)
        empty_bst.node = Node(18, None, None)


        self.assertEqual(insert(bst, 18), inserted_bst)
        self.assertEqual(insert(BinarySearchTree(comes_before), 18), empty_bst)

    def test_get_node(self):
        def comes_before(a, b):
            return a < b

        target_node =   Node(11, 
                            Node(9, 
                                Node(8, None, None),
                                None),
                            Node(16, None, None)
                            )

        self.assertEqual(get_node(self.bst_node, comes_before, 11), target_node)

    def test_lookup(self):
        def comes_before(a, b):
            return a < b

        bst = BinarySearchTree(comes_before)
        bst.node = self.bst_node

        self.assertTrue(lookup(bst, 11))
        self.assertFalse(lookup(bst, 127))

    def test_delete(self):
        def comes_before(a, b):
            return a < b

        bst = BinarySearchTree(comes_before)
        bst.node = self.bst_node

        after_delete_8_bst_nodes = Node(17, 
                                Node(5, 
                                    Node(2, None, None),
                                    Node(11, 
                                        Node(9, 
                                            None,
                                            None),
                                        Node(16, None, None)
                                        )
                                    ),
                                Node(35, 
                                    Node(29, None, None),
                                    Node(38, None, None)
                                    )
                                )

        after_delete_8_bst = BinarySearchTree(comes_before)
        after_delete_8_bst.node = after_delete_8_bst_nodes

        after_delete_all_nodes = Node(29, 
                                Node(5, 
                                    Node(2, None, None),
                                    Node(11, 
                                        Node(9, 
                                            None,
                                            None),
                                        Node(16, None, None)
                                        )
                                    ),
                                Node(35, 
                                    None,
                                    Node(38, None, None)
                                    )
                                ) 
        after_delete_all = BinarySearchTree(comes_before)
        after_delete_all.node = after_delete_all_nodes

        self.assertEqual(delete(bst, 8), after_delete_8_bst)
        self.assertEqual(delete(bst, 17), after_delete_all)

if __name__ == '__main__':
    unittest.main()