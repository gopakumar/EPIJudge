from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.
    global result
    result = True
    def helper(node: BinaryTreeNode) -> int:
        if not node:
            return 0
        lft = helper(node.left)
        rht = helper(node.right)
        global result
        if  abs(lft-rht) > 1 :
            #print("setting to false")
            result = False
        return 1+ max(lft,rht)
    helper(tree)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
