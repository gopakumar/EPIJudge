import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def reconstruct_preorder(preorder: List[int]) -> BinaryTreeNode:
    # TODO - you fill in here.
    '''
    if len(preorder) == 0:
        return None
    root = BinaryTreeNode(preorder[0])
    nodes = []
    nodes.append(root)
    i = 1
    while nodes:
        node = nodes.pop(0)
        if preorder[i] and preorder[i] != 'null':
            tlnode = BinaryTreeNode(preorder[i])
            node.left = tlnode
            nodes.append(tlnode)
        i+=1
        if preorder[i] and preorder[i] != 'null':
            trnode = BinaryTreeNode(preorder[i])
            node.right = trnode
            nodes.append(trnode)
        i+=1
        #nodes = tempnodes[:]
    
    return root
'''
    global i
    i = 0
    def helper():
        global i
        if  not preorder[i] or  preorder[i] == 'null':
            return None
        node = BinaryTreeNode(preorder[i])
        i+=1
        node.left = helper()
        i+=1
        node.right= helper()
        return node
    return helper()

@enable_executor_hook
def reconstruct_preorder_wrapper(executor, data):
    data = [None if x == 'null' else int(x) for x in data]
    return executor.run(functools.partial(reconstruct_preorder, data))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_with_null.py',
                                       'tree_from_preorder_with_null.tsv',
                                       reconstruct_preorder_wrapper))
