'''
Question: https://leetcode.com/problems/decode-ways/ 
'''

class Solution:
    # def numDecodings(self, s: str) -> int:
    #     '''Approach 1: Recursion - more space complexity'''
    #     n = len(s)
    #     dp = {n: 1}

    #     def dfs(i):
    #         '''Helper Function'''
    #         # Base case: if i already present in `dp`
    #         if i in dp: return dp[i]

    #         # Base case: if invalid string 
    #         if s[i] == "0": return 0

    #         # for single digit problem, check the next number
    #         res = dfs(i + 1)

    #         # for double digit problem
    #         # condition: 1. if two digits present
    #         #            2. if the two digit number is between 10 and 26
    #         if ((i + 1 < n) and 
    #             (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456")):
    #             # # If yes, then check for the two digits problem
    #             res += dfs(i + 2)

    #         # Remember to store the result in the dp
    #         dp[i] = res
    #         return res
        
    #     # Run the dfs starting from index 0
    #     return dfs(0)
            

    def numDecodings(self, s: str) -> int:
        '''Approach 2: Dynamic Programming - less space complexity'''

        n = len(s)
        # Split into subproblems, save in a DP of size = len(s), init all values to 1
        dp = {n : 1}
        
        # Here we iterate in reverse (solve subproblems) and store the results in dp, building up to index 0
        for i in range(n-1, -1, -1):
            
            # Base cases where the answer is "0" i.e. invalid character
            if s[i] == "0":
                dp[i] = 0
                
            # Here, check for one digit case (only one char)
            # Save the value stored dp (from a previous subproblem - memoization)
            else:                
                dp[i] = dp[i+1]

           # for double digit problem
            # condition: 1. if two digits present
            #            2. if the two digit number is between 10 and 26
            if ((i + 1 < n) and 
                (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456")):
                dp[i] += dp[i+2]
        
        # Return the result stored in dp at index 0 (since we iterate in reverse, result will be 
        # saved in dp[0] in the end)
        return dp[0]