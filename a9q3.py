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


def expression(tnode):
    """
    Purpose:
        Produces a string representation of an input mathematical formula represented by an expression tree.
    Pre-conditions:
        :param tnode: a tree node
    Post-conditions:
        None
    Return:
        A string representation of the of the mathematical formula represented by an expression tree.
    """
    if tnode is None:
        return ''
    else:
        left_string = expression(tnode.left)
        right_string = expression(tnode.right)
        return '(' + str(left_string) + str(tnode.data) + str(right_string) + ')'
