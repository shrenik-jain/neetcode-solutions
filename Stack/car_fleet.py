'''
Question: https://leetcode.com/problems/car-fleet/
'''

from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        TC: O(n) [iteration] + O(nlogn) [sorting] = O(nlogn)
        SC: O(n)
        '''
        # create pairs of position and speed of the cars
        pairs = [[p, s] for p, s in zip(position, speed)]
        # to maintain the number of car fleets
        stack = []

        # iterate over sorted `pairs` in reverse order
        for p, s in sorted(pairs)[::-1]:

            # find the timeTaken by ith car to reach the target using distance formula (T = D/S)
            timeTaken = (target - p) / s
            # Append the timeTaken by the ith car to the stack
            stack.append(timeTaken)

            # NOTE: If the car behind is going to reach the target faster than the 
            # car ahead, there will be a collision, hence pop the faster car

            # if the newly appended timeTaken (by car behind, since reverse iteration)
            # is less than the previous car (the car ahead, since reverse iteration), pop the faster car
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        # the number of cars remaining in the stack will be equal to the number of fleets
        return len(stack)