'''
Question: https://leetcode.com/problems/insert-interval/
'''

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ''' 
        When inserting, check if they are merging.
        If they are, the new interval is the `min of starts` and `max of ends`

        How to check where to add the new interval (in case of no-overlap)?
                                        IF
        - end of new interval < start of curr interval, then add before 
                                      ELSE IF
        - start of new interval > end of curr interval, then add after
        
        Time Complexity = O(n) 
        '''
        res = []

        for i, intv in enumerate(intervals):
            # if end-time of newInterval < start-time of ith interval i.e. newInterval occurs before ith interval
            # No overlap, to be merged before current interval
            if newInterval[1] < intv[0]:
                # add the newInterval first
                res.append(newInterval)
                # Since newInterval occurs before ith interval, no further intervals will overlap with newInterval,
                # hence add the remaining intervals to `res`
                return res + intervals[i:]

            # if start-time of newInterval > end-time of ith interval i.e. newInterval occurs after ith interval
            # No overlap, new to be merged after current interval
            elif newInterval[0] > intv[1]:
                # Here we add the current interval, and keep checking since the newInterval
                # could be merged AFTER other intervals too!
                res.append(intv)

            # Overlap case, we create the new merged interval - min of starts and max of ends
            else:
                # 
                newInterval = [ min(newInterval[0], intv[0]),
                                max(newInterval[1], intv[1]) ]

        # We add the new merged interval to the result (for elif and else cases)
        res.append(newInterval)
            
        return res
