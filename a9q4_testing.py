"""
    Name: Allen Keettikkal
    NSID: alk423
    Student Number: 11278995
    Instructor: Jeffrey Long
"""

import a9q4 as tn

# ####################################################################################################
# #### UNIT TEST CASE: expression() ####

test_item = 'complete()'

test_suite = [
    {
        'tree in': None,
        'subtree height': None,
        'expected boolean': False,
        'reason': 'No tree in.'
    },

    {
        'tree in': tn.treenode(1),
        'subtree height': 1,
        'expected boolean': True,
        'reason': 'No tree in.',
    },

    {
        'tree in': tn.treenode(1, tn.treenode(2)),
        'subtree height': None,
        'expected boolean': False,
        'reason': 'No tree in.',
    },

    {
        'tree in': tn.treenode(1, tn.treenode(2), tn.treenode(3)),
        'subtree height': 2,
        'expected boolean': True,
        'reason': 'No tree in.',
    },

    {
        'tree in':  tn.treenode(1, tn.treenode(2, tn.treenode(2), tn.treenode(3)), tn.treenode(4, tn.treenode(4), tn.treenode(5))),
        'subtree height': 2,
        'expected boolean': True,
        'reason': 'No tree in.',
    }
]

for test in test_suite:
    tree_in = test['tree in']
    subtree_height = test['subtree height']
    expected_bool = test['expected boolean']
    reason = test['reason']
    result_str = tn.complete(tree_in)
    if result_str != (subtree_height, expected_bool):
        print('Test failed: {}: got "{}", "{}" expected "{}", "{}" -- {}'.format(test_item, result_str[0], result_str[1], subtree_height, expected_bool, reason))