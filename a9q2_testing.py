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
import treefunctions

# ####################################################################################################
# #### UNIT TEST CASE: replace_in() ####
test_item = "replace_in()"

tree_in = None
target_in = 1
repl_in = 0
expected_str = "EMPTY"
reason = 'empty tree'

tn.subst(tree_in, target_in, repl_in)
result_str = treefunctions.to_string(tree_in)
if result_str != expected_str:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result_str, expected_str, reason))

