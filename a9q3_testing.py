"""
    Name: Allen Keettikkal
    NSID: alk423
    Student Number: 11278995
    Instructor: Jeffrey Long
"""

import a9q3 as tn
import treefunctions as tf

# ####################################################################################################
# #### UNIT TEST CASE: expression() ####

test_item = 'expression()'

test_suite = [
    {
        'tree in': None,
        'expected string': '',
        'reason': 'Empty string.'
    },

    {
        'tree in': tn.treenode(2),
        'expected string': '(2)',
        'reason': 'Prints out the leaf node.'
    },

    {
        'tree in': tn.treenode('+', tn.treenode(2), tn.treenode(3)),
        'expected string': "((2)+(3))",
        'reason': 'The main node is the +, accompanying it is the 2 on the left and the 3 on the right.'
    },

    {
        'tree in': tn.treenode('*', tn.treenode('+', tn.treenode(2), tn.treenode(3)), tn.treenode('-', tn.treenode(4), tn.treenode(5))),
        'expected string': "(((2)+(3))*((4)-(5)))",
        'reason': 'Empty string.'
    }
]

for test in test_suite:
    tree_in = test['tree in']
    expected_str = test['expected string']
    reason = test['reason']
    result_str = tn.expression(tree_in)
    if result_str != expected_str:
        print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result_str, expected_str, reason))