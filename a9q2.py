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

    def subst(self, tnode, target, replacement):
        """
        Purpose:
            Replaces each occurrence of the target value with the replacement
        Pre-conditions:
            :param node_chain: a node-chain, possibly empty
            :param target: a value that might appear in the node chain
            :param replacement: the value to replace the target
        Pre-conditions:
            Each occurrence of the target value in the chain is replaced with
            the replacement value.
        Return:
            None
        """
        # walk along the chain
        if tnode is None:
            return "EMPTY"
        else:
            while tnode is not None:
                if tnode.get_data() == target:
                    tnode.set_data(replacement)
                tnode = tnode.get_next()
        return None

    def copy(self, tnode):
        return None

    def collect_data_inorder(self, tnode):
        return list

    def count_smaller(self, tnode, target):
        return target
