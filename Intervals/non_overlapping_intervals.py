'''
Question: https://leetcode.com/problems/non-overlapping-intervals/
'''

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        Sorting ensures that we just compare adjacent pairs of intervals,
        instead of restarting the iteration everytime we merge two intervals and then restart until 
        we find no more overlapping intervals. This approach would lead to O(n^2) time complexity.

        Whenever we find two overlapping intervals, we need to remove the one that ends first, since we are
        minimizing the chances of overlap with the next interval and hence the minimize number of removals.
        '''
        # sort the intervals based on start time
        intervals.sort(key=lambda i : i[0])
        num_removals = 0
        # keep track of the previously occuring end time (at the beginning init to first interval end time)
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            # No overlap case, since start of current interval is after the end of the previous interval
            if start >= prevEnd:
                # simply update the previous end to current end (keep track of last interval end time)
                prevEnd = end

            # overlap case
            else:
                # we have to remove one of the intervals, hence increment `num_removals`
                num_removals += 1
                # keep the one that ends first
                prevEnd = min(prevEnd, end)

        return num_removals
    

