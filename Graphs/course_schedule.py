"""
Question: https://leetcode.com/problems/course-schedule
"""

from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        Use DFS to check if each course can be completed

        Time Complexity: O(course + prerequisites)
        Space Complexity: O(course)
        '''
        # create a hashmap (adjacency list) to map courses to its prereqs {1: [0, 2], 1: [3]....}
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # the keep track of all the courses along the DFS path (Basically to detect if a loop exisits)
        visitSet = set()

        def dfs(crs):
            # we have encountered a course which we previously saw along the DFS path (a loop exists) -> return False
            if crs in visitSet:
                return False

            # the current course does not have any prereqs, hence can be completed -> return True
            if preMap[crs] == []:
                return True

            # add the current course in the visitSet
            visitSet.add(crs)

            # go through all the prerqs of the current course `crs`
            for pre in preMap[crs]:
                # if a certain prereq cannot be completed, return False immediately
                if not dfs(pre): return False
            
            # if above loop executes without returning anything, means all prereqs can be completed, 
            # hence empty the current course prereqs
            preMap[crs] = []
            # remove the course from visitSet, since it can be completed successfully
            visitSet.remove(crs)

            return True

        # go through all the courses and check if they can completed
        for crs in range(numCourses):
            # if one of the courses cannot be completed, return False immediately
            if not dfs(crs): return False

        # if above loop executes perfectly, then all courses can be completed -> return True
        return True
        