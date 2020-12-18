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

    '''memo = [[0 for _ in range(final_score+1)] for i in range(len(individual_play_scores)+1)]
    def helper1 (score:int, runs:List[int]) -> int:
        #print(score,len(runs))
        
        # TODO - you fill in here.
        if score == 0:
            return 1
        elif score < 0:
            return 0
        tval = memo[len(runs)][score]
        if tval > 0:
            return tval

        ret = 0
        for i in range(len(runs)):
            ind = runs[i]
            ret += helper1(score - ind,runs[i:])
        memo[len(runs)][score] = ret
        #print (len(runs),score,ret)
        return ret

    result =  helper1(final_score,individual_play_scores[:])
    #print(memo)
   '''
    return helper(final_score,individual_play_scores[:])
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))

