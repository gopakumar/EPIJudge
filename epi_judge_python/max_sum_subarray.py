from typing import List

from test_framework import generic_test


def find_maximum_subarray(A: List[int]) -> int:
    # TODO - you fill in here.
    tmax = 0
    cmax = 0
    csum = 0
    for a in A:
        if a > (a+csum):
            csum =a
        else:
            csum+=a
        tmax = max(csum,tmax)



        
    return tmax


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_sum_subarray.py',
                                       'max_sum_subarray.tsv',
                                       find_maximum_subarray))
