from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def has_path_sum(tree: BinaryTreeNode, remaining_weight: int) -> bool:
    # TODO - you fill in here.
    if not tree:
        return False
    rem = remaining_weight - tree.data
    if not tree.left and not tree.right:
        if rem == 0:
            return True
        else:
            return False

    return has_path_sum(tree.left,rem) or has_path_sum(tree.right, rem)
        


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('path_sum.py', 'path_sum.tsv',
                                       has_path_sum))
