'''
Question: https://leetcode.com/problems/task-scheduler/
'''

import heapq
from typing import List
from collections import Counter, deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Maintain a maxHeap to complete most frequent tasks first

        Time Complexity: O(n) + O(nlogn)
        Space Complexity: O(n)
        """
        # count the frequency of each task
        count = Counter(tasks)
        # store the count of each task in a maxHeap (-cnt since maxHeap)
        maxHeap = [-cnt for cnt in count.values()]
        # make it a maxHeap
        heapq.heapify(maxHeap)

        # maintain a queue to keep track of remaining cnt and next available time of each task
        q = deque() # stores [-cnt, next time when available]
        
        # var to keep track of unit time
        time = 0

        # while tasks are present either in the maxHeap or the q
        while maxHeap or q:
            # increment the time unit by 1
            time += 1

            # if tasks available in the maxHeap
            if maxHeap:
                # pop the most-frequent task and add 1 to it (basically reduce the 
                # freq, but since -cnt, hence +1)
                cnt = 1 + heapq.heappop(maxHeap)

                # if the cnt is not 0 (the task has freq remaining)
                if cnt:
                    # push the new cnt, next time it will be available (curr_time + idle_time)
                    q.append([cnt, time + n])

            # if the queue has tasks, and any task from the queue if available at curr time `time`
            if q and q[0][1] == time:
                # pop it from the q, and add it to the maxHeap
                heapq.heappush(maxHeap, q.popleft()[0])

        # after above loop is complete, all tasks has been processed, return the total_time
        return time

        