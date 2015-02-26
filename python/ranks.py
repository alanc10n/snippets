"""
Rank Vectors

Given an array (or list) of scores, return the array of ranks for each value in the array. The largest value has rank 1, the second largest value has rank 2, and so on. Ties should be handled by assigning the same rank to all tied values. For example:

ranks([9,3,6,10]) = [2,4,3,1] and ranks([3,3,3,3,3,5,1]) = [2,2,2,2,2,1,7]
ranks([8, 98, 10, 3, 3, 4, 4, 89]) # [4, 1, 3, 7, 7, 5, 5, 2]
"""


def ranks(scores):
    """ Slick solution using the offset in the sorted list of the first occurence
        to determine the rank.
    """
    sorted_scores = sorted(scores, reverse=True)
    rank_list = [sorted_scores.index(n) + 1 for n in scores]
    return rank_list


if __name__ == '__main__':
    instr = raw_input('Enter comma-separated numbers (e.g. 3,5,2)')
    scores = [int(n) for n in instr.split(',')]
    print 'Ranking {0}'.format(scores)
    ret = ranks(scores)
    print 'Ranks: {0}'.format(ret)

