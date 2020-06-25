"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        # if value < self.value and self.left is None:
        #     self.left = BSTNode(value)
        # if value >= self.value and self.right is None:
        #     self.right = BSTNode(value)

        # if value is < less than self.value
        if value < self.value:
            # go left
            # check if left has value
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

            # go right
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        # compare the target to current value
        # if current value >= target
        # found = False
        if self.value >= target:
            # check the left subtree
            # if you cannot go left, return false
            if self.left is None:
                return False
            found = self.left.contains(target)
        else:
            # check if right subtree contains target
            # if you cannot go right, return false
            if self.right is None:
                return False
            found = self.right.contains(target)

        return found

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        return self.right.get_max()
        # check that there are values on right
        # while there are values

        # current = self
        #
        # while current.right is not None:
        #     current = current.right
        # return current.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        # if exists check left
        if self.left is not None:
            # call .for_each(fn)
            self.left.for_each(fn)
        # check right
        if self.right is not None:
            # call .for_each(fn)
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node=None):
        # if self has a 'left', self is BIGGER
        if self.left:
            self.left.in_order_print(self)

        print(self.value)

        # if self has a 'right', self is SMALLER
        if self.right:
            self.right.in_order_print(self)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node=None):
        # create a queue for nodes
        que = [self]
        # add the first node to the queue
        # while queue is not empty
            # remove the first node from the queue
            # print the removed node
            # add all children into the queue
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # create a stack for nodes
        # add the first node to the stack
        # while the stack is not empty
            # get the current node from teh top of the stack
            # print that node
            # add all children to the stack
            # keep in mind, the order you add the children, will matter
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

bst = BSTNode(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)
bst.bft_print()
