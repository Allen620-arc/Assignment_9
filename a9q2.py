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

    def subst(self, tnode, t, r):
        return None

    def copy(self, tnode):
        return None

    def collect_data_inorder(self, tnode):
        return list

    def count_smaller(self, tnode, target):
        return target

        


