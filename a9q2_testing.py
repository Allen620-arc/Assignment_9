# CMPT 145 Course material
# Copyright (c) 2017-2020 Michael C Horsch
# All rights reserved.
#
# This document contains resources for homework assigned to students of
# CMPT 145 and shall not be distributed without permission.  Posting this 
# file to a public or private website, or providing this file to a person 
# not registered in CMPT 145, constitutes Academic Misconduct, according 
# to the University of Saskatchewan Policy on Academic Misconduct.
# 
# Synopsis:
#   Defines a few example trees

import a9q2 as tn
import treefunctions as tf

# ####################################################################################################
# #### UNIT TEST CASE: replace_in() ####

test_item = 'replace_in()'

test_suite = [
    {
        'tree in': None,
        'target in': 1,
        'repl in': 0,
        'expected str': "EMPTY",
        'reason': 'empty tree'
    },

    {
        'tree in': tn.treenode(1),
        'target in': 1,
        'repl in': 0,
        'expected str': '0\n',
        'reason': 'tree with one node, target replaced 1 with 0'
    },

    {
        'tree in': tn.treenode(1),
        'target in': 0,
        'repl in': 1,
        'expected str': '1\n',
        'reason': 'node chain with one node, target not present'
    },

    {
        'tree in': tn.treenode(1, tn.treenode(2)),
        'target in': 1,
        'repl in': 10,
        'expected str': '10\n\t2\n',
        'reason': 'node chain with two nodes, target present first'
    },

    {
        'tree in': tn.treenode(1, tn.treenode(2)),
        'target in': 1,
        'repl in': 10,
        'expected str': '10\n\t2\n',
        'reason': 'node chain with two nodes, target present first'
    },

    {
        'tree in': tn.treenode(1, tn.treenode(2, tn.treenode(3))),
        'target in': 1,
        'repl in': 10,
        'expected str': '10\n\t2\n\t\t3\n',
        'reason': 'node chain with two nodes, target present first'
    }
]

for test in test_suite:
    tree_in = test['tree in']
    target_in = test['target in']
    repl_in = test['repl in']
    expected_str = test['expected str']
    reason = test['reason']
    tn.subst(tree_in, target_in, repl_in)
    result_str = tf.to_string(tree_in)
    if result_str != expected_str:
        print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result_str, expected_str, reason))

# ####################################################################################################
# #### UNIT TEST CASE: copy() ####

test_item = 'copy()'

test_suite = [
    {
        'tree in': None,
        'expected tree': None,
        'reason': 'empty tree'
    },

    {
        'tree in': tn.treenode(1),
        'expected tree': tn.treenode(1),
        'reason': 'copied tree with one node'
    },

    {
        'tree in': tn.treenode(1, tn.treenode(2)),
        'expected tree': tn.treenode(1, tn.treenode(2)),
        'reason': 'copied tree with two nodes'
    },

    {
        'tree in': tn.treenode(1, tn.treenode(2, tn.treenode(3))),
        'expected tree': tn.treenode(1, tn.treenode(2, tn.treenode(3))),
        'reason': 'copied tree with two nodes'
    }
]

for test in test_suite:
    tree_in = test['tree in']
    expected_tree = test['expected tree']
    reason = test['reason']
    output_tree = tn.copy(tree_in)
    expected_string = tf.to_string(expected_tree)
    output_string = tf.to_string(output_tree)
    if output_string != expected_string:
        print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, output_string, expected_string, reason))

# ####################################################################################################
# #### UNIT TEST CASE: collect_data_inorder() ####

test_item = 'collect_data_inorder(tnode)'

test_suite = [
    {
        'tree in': None,
        'expected list': [],
        'reason': 'empty tree'
    },

    {
        'tree in': tn.treenode(1),
        'expected list': [1],
        'reason': 'copied tree with one node'
    },

    {
        'tree in': tn.treenode(1, tn.treenode(2)),
        'expected list': [1, 2],
        'reason': 'copied tree with two nodes'
    },

    {
        'tree in': tn.treenode(1, tn.treenode(2, tn.treenode(3))),
        'expected list': [1, 2, 3],
        'reason': 'copied tree with two nodes'
    }
]

for test in test_suite:
    tree_in = test['tree in']
    expected_list = test['expected list']
    reason = test['reason']
    output_list = tn.collect_data_inorder(tree_in)
    if output_list != expected_list:
        print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, output_list, expected_list, reason))