# A BSTNode is one of:
# - None
# - Node(value, BSTNode, BSTNode)
class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def __eq__(self, other):
        return ((type(other) == Node)
          and self.value == other.value
          and self.left == other.left
          and self.right == other.right
        )

    def __repr__(self):
        return ("Node({!r}, {!r}, {!r})".format(self.value, self.left, self.right))

# A BinarySearchTree is BinarySearchTree(BSTNode, comes_before)
class BinarySearchTree:
    def __init__(self, comes_before):
        self.node = None
        self.comes_before = comes_before

    def __eq__(self, other):
        return ((type(other) == BinarySearchTree)
          and self.comes_before == other.comes_before
        )

    def __repr__(self):
        return ("BinarySearchTree({!r})".format(self.node))

# BinarySearchTree -> Bool
# Checks whether the tree is empty
def is_empty(bst):
    return bst.node is None

# BinarySearchTree, Any -> BinarySearchTree
# Inserts a value into its correct position in the tree
def insert(bst, new_val):
    bst.node = insert_node(bst.node, new_val, bst.comes_before)
    return bst

# BSTNode, func -> BSTNode
# Helper for insert() -- Inserts and returns node at its proper spot
def insert_node(node, new_val, comes_before):
    if node is None:
        return Node(new_val, None, None)
    else:
        if comes_before(new_val, node.value):
            return Node(node.value, insert_node(node.left, new_val, comes_before), node.right)
        else:
            return Node(node.value, node.left, insert_node(node.right, new_val, comes_before))

# BinarySearchTree, Any, func -> BSTNode
# General Helper -- Returns target node if found, None if not found
def get_node(node, comes_before, target):
    if node is None:
        return None
    else:
        if comes_before(target, node.value):
            return get_node(node.left, comes_before, target)
        elif comes_before(node.value, target):
            return get_node(node.right, comes_before, target)
        else:
            return node

# BinarySearchTree, Any -> Bool
# Checks whether a given value is in the tree
def lookup(bst, target):
    return get_node(bst.node, bst.comes_before, target) is not None

# BinarySearchTree, Any -> BinarySearchTree
# Removes the given value from the tree
def delete(bst, target):
    bst.node = delete_node(bst.node, bst.comes_before, target)
    return bst

# BSTNode, func, Any -> BSTNode
# Helper for delete() -- Deletes the target node and returns the new root node of the tree
def delete_node(node, comes_before, target):
    if node is None:
        return None
    else:
        if comes_before(target, node.value):
            return Node(node.value, delete_node(node.left, comes_before, target), node.right)
        elif comes_before(node.value, target):
            return Node(node.value, node.left, delete_node(node.right, comes_before, target))
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                replacement_value = get_min_right_value(node.right)
                node.right = delete_node(node.right, comes_before, replacement_value)
                node.value = replacement_value
                return node

# BSTNode -> value
# Returns the smallest node in the tree and its parent
def get_min_right_value(node):
    if node.left is None:
        return node.value
    else:
        return get_min_right_value(node.left)

# BinarySearchTree -> Iterator
# Returns an iterator of elements in prefix order wherein, for a given node, the node is visited before its children
def prefix_iterator(bst):
    current_node = bst.node
    left_bst = BinarySearchTree(bst.comes_before)
    left_bst.node = current_node.left
    right_bst = BinarySearchTree(bst.comes_before)
    right_bst.node = current_node.right

    if current_node is not None:
        try:
            yield current_node.value
            yield from prefix_iterator(left_bst)
            yield from prefix_iterator(right_bst)
        except:
            raise StopIteration


# BinarySearchTree -> Iterator
# Returns an iterator of the elements in infix order wherein, for a given node, the node is visited after its left child but before its right child.
def infix_iterator(bst):
    if bst.node is not None:
        left_bst = BinarySearchTree(bst.comes_before)
        left_bst.node = bst.node.left
        yield from infix_iterator(left_bst)

        yield bst.node.value

        right_bst = BinarySearchTree(bst.comes_before)
        right_bst.node = bst.node.right
        yield from infix_iterator(right_bst)

# BinarySearchTree -> Iterator
# Returns an iterator of the elements in postfix order wherein, for a given node, the node is visited after its children
def postfix_iterator(bst):
    if bst.node is not None:
        left_bst = BinarySearchTree(bst.comes_before)
        left_bst.node = bst.node.left

        right_bst = BinarySearchTree(bst.comes_before)
        right_bst.node = bst.node.right

        yield from postfix_iterator(left_bst)
        yield from postfix_iterator(right_bst)
        yield bst.node.value
