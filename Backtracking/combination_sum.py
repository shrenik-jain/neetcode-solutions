'''
Question: https://leetcode.com/problems/combination-sum/
'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ''' 
        Perform a DFS on the given list of candidates 
        TC: O(2^n)
        '''
        res = []

        # Helper function for DFS
        def dfs(i, cur, total):
            # Base Case if total of curr matches the target
            if total == target:
                res.append(cur.copy())
                return

            # Base Case if we have reached the last candidate or if total > target
            if i >= len(candidates) or total > target:
                return

            # First decision
            # we append the current candidate to `cur`
            cur.append(candidates[i])
            # since we append the current candidate, `i` does not change and we add current candidate to `total`
            dfs(i, cur, total + candidates[i])
            # we are moving to next decision, hence we remove the current candidate we appended above
            cur.pop()
            
            # Second Decision 
            # We move to the next candidate i.e. do not add the current candidate
            dfs(i + 1, cur, total)


        # Pass 3 params
        # i -> ith candidate (starts with the 0th candidate)
        # cur -> current list of candidates
        # total -> sum of cur list of candidates 
        dfs(0, [], 0)
        return res       