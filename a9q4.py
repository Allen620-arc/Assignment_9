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


def complete(tnode):
    """
    Purpose:
        To check if the binary tree is a complete binary tree.
    Pre-conditions:
        :param tnode: a tree node
    Post-conditions:
        None
    Return:
        A boolean value, either True or False.
    """
    def cmplt(tnode):
        """
        Purpose:
            To check if the binary tree is a complete binary tree.
        Pre-conditions:
            :param tnode: a tree node
        Post-conditions:
            None
        Return:
            A boolean value, either True or False.
        """
        if tnode is None:
            return None, False
        else:
            lflag, ldepth = cmplt(tnode.left)
            rflag, rdepth = cmplt(tnode.right)
            if ldepth == rdepth:
                return rdepth + 1, True
            else:
                return None, False
    return cmplt(tnode)