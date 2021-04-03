"""
    Name: Allen Keettikkal
    NSID: alk423
    Student Number: 11278995
    Instructor: Jeffrey Long
"""

class treenode(object):

    def __init__(self, data, left=None, right=None):
        """
        Create a new treenode for the given data.
        Pre-conditions:
            data:  Any data value to be stored in the treenode
            left:  Another treenode (or None, by default)
            right:  Another treenode (or None, by default)
        """
        self.data = data
        self.left = left
        self.right = right


def ordered(tnode):
    """
    Purpose:
        To check if the treenode is ordered.
    Pre-conditions:
        :param tnode:
    Post-condtions:

    Return:

    """
    if tnode is None:
        return True
    if tnode.left is None:
        return True
    if tnode.right is None:
        return True
    if tnode.left > tnode.data > tnode.right:
        return True
    else:
        left_order = ordered(tnode.left)
        right_order = ordered(tnode.right)
        return left_order and right_order
