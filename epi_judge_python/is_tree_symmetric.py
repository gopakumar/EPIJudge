from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.
    def helper(left: BinaryTreeNode, right:BinaryTreeNode) -> bool:
        if not left and not right:
            return True

        if not left or not right:
            return False

        return ((left.data == right.data) and helper(left.left, right.right) and helper(left.right, right.left))

    if not tree:
        return True
    return helper(tree.left, tree.right)



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
