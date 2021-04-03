"""
    Name: Allen Keettikkal
    NSID: alk423
    Student Number: 11278995
    Instructor: Jeffrey Long
"""

import a9q5 as tn

# ####################################################################################################
# #### UNIT TEST CASE: ordered() ####

test_item = 'ordered()'

test_suite = [
    {
        'tree in': None,
        'ordered': True,
        'reason': 'No tree in.'
    },

    {
        'tree in': tn.treenode(1),
        'ordered': True,
        'reason': 'Only a Root Node.',
    },

    {
        'tree in': tn.treenode(1, tn.treenode(2)),
        'ordered': True,
        'reason': 'Only one left Node.',
    },

    {
        'tree in': tn.treenode(1, tn.treenode(2), tn.treenode(3)),
        'ordered': True,
        'reason': 'Only one left and right Node.',
    },

    {
        'tree in':  tn.treenode(1, tn.treenode(2, tn.treenode(2), tn.treenode(3)), tn.treenode(4, tn.treenode(4), tn.treenode(5))),
        'ordered': True,
        'reason': 'The values get progressively bigger overtime',
    }
]

for test in test_suite:
    tree_in = test['tree in']
    ordered = test['ordered']
    reason = test['reason']
    result_str = tn.ordered(tree_in)
    if result_str != ordered:
        print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result_str, ordered, reason))