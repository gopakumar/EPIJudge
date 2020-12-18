from typing import List

from test_framework import generic_test


def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    myd={}

    def helper (score:int, runs:List[int]) -> int:
        if((score,len(runs)) in myd ):
            return myd[(score,len(runs))]

        # TODO - you fill in here.
        if score == 0:
            return 1
        elif score < 0:
            return 0
        ret = 0
        for i in range(len(runs)):
            ind = runs[i]
            ret += helper(score - ind,runs[i:])
        myd[(score,len(runs))] = ret
        return ret


    return helper(final_score,individual_play_scores[:])

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))

