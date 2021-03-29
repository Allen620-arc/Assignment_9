
def bad_complete(tnode):
    def cmplt(tnode):
        if tnode is None:
            return 0
        else:
            ldepth = cmplt(tnode.left)
            rdepth = cmplt(tnode.right)
            if ldepth == rdepth:
                return rdepth+1
            else:
                return -1
    result = cmplt(tnode)
    return result > 0
