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


def subst(tnode, target, replacement):
    """
    Purpose:
        Replaces each occurrence of the target value with the replacement
    Pre-conditions:
        :param tnode: a tree node
        :param target: a value that might appear in the node chain
        :param replacement: the value to replace the target
    Post-conditions:
        Each occurrence of the target value in the chain is replaced with the replacement value.
    Return:
        None, but modifies the given tree.
    """
    if tnode is None:
        return None
    else:
        if tnode.data is target:
            tnode.data = replacement
        subst(tnode.left, target, replacement)
        subst(tnode.right, target, replacement)


def copy(tnode):
    """
    Purpose:
        To create an exact copy of the given tree, with completely new tree nodes, but exactly the same data values.
    Pre-conditions:
        :param tnode: a tree node
    Post-conditions:
         None.
    Return:
        A reference to the new tree if tnode has values.
    """
    if tnode is None:
        return None
    else:
        return treenode(tnode.data, tnode.left, tnode.right)


def collect_data_inorder(tnode):
    """
    Purpose:
        To collect all the data values in the given tree.
    Pre-conditions:
        :param tnode: a tree node
    Post-conditions:
         None.
    Return:
        A list of all the data values, and the data values appear in the list according to the in-order sequence.
    """
    if tnode is None:
        return []
    else:
        collect_data_inorder(tnode.left)
        collect_data_inorder(tnode.right)
        return [tnode.data] + collect_data_inorder(tnode.left) + collect_data_inorder(tnode.right)


def count_smaller(tnode, target):
    """
    Purpose:
        Count the number of data values in the given tree that are less than the given target value.
    Pre-conditions:
        :param tnode: a tree node
        :param target: a value that might appear in the node chain
    Post-conditions:
        None.
    Return:
        The number of values less than target.
    """

    return target
