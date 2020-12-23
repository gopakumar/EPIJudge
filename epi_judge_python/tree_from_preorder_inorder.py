from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    # TODO - you fill in here.
    if len(preorder) ==0:
        return None
    data = preorder[0]
    leftlen = 0
    rightlen = 0
    for x in range(len(inorder)):
        if inorder[x] == data:
            leftlen = x
    rightlen = len(inorder)-leftlen-1

    leftlink = binary_tree_from_preorder_inorder(preorder[1:leftlen+1],inorder[:leftlen+1])
    rightlink = binary_tree_from_preorder_inorder(preorder[1+leftlen:],inorder[leftlen+1:])
    node = BinaryTreeNode(data,leftlink,rightlink)
    return node


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
