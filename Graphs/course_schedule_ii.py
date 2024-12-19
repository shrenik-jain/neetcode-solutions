"""
Question: https://leetcode.com/problems/course-schedule-ii/
"""

from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Use to check if each course can be completed

        Time Complexity: O(course + prerequisites)
        Space Complexity: O(course)
        """
        # create a hashmap (adjacency list) to map courses to its prereqs {1: [0, 2], 1: [3]....}
        preMap = {i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            preMap[c].append(p)

        # `visit set` will keep track of courses which have already been completed
        # `cycle set` will keep track of any loops or cycles that exist
        visit, cycle = set(), set()
        # to store the final order in which courses should be taken
        order = []

        def dfs(crs):
            # we encountered a course which we previously saw along the DFS path (a loop exists)
            if crs in cycle:
                return False

            # the current course has already been completed -> return True
            if crs in visit:
                return True
            
            # add the current course in the cycle set
            cycle.add(crs)

            # go through all the prerqs of the current course `crs`
            for pre in preMap[crs]:
                # if a certain prereq cannot be completed, return False immediately
                if not dfs(pre): return False
            
            # if above loop executes without returning anything, means all prereqs can be completed, 
            # hence remove the current course from cycle set
            cycle.remove(crs)
            # hence add the current course to the visit set (can be successfully completed)
            visit.add(crs)
            # hence add the current course to the order list
            order.append(crs)
            # hence return True (can be successfully completed)
            return True

        # go through all the courses and check if they can completed
        for crs in range(numCourses):
            # if one of the courses cannot be completed, return [] immediately
            if not dfs(crs): return []

        # if above loop executes perfectly, then all courses can be completed -> return order
        return order
