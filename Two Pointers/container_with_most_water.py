'''
Question: https://leetcode.com/problems/container-with-most-water/
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        Keep two pointers left and right (since we want to maximize the width). 
        Keep calculating area between these two pointers to find maxArea
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        # init left pointer `l` to the start of list
        # init right pointer `r` to the end of the list
        l, r = 0, len(height)-1
        maxWater = 0
        
        # keep caclulating until both pointer meet or cross each other
        while(l < r):
            # the height of container will depend on the shorter height between `l` and `r`
            # see visually in the description image
            container_height = min(height[l], height[r])

            # the width will be number of compartments between right and left pointers
            # see visually in the description image
            container_width = r - l

            # calculate the area of rectangular container using formula a= height x width
            curr_maxWater =  container_height * container_width 

            # check if current area is greater than previous all areas of water
            maxWater = max(maxWater, curr_maxWater)

            # we move to the next container from the one with the shorter height 
            # so that we can maximize the length of the container and hence maximize the area
            # if left is shorter, increment left to next height 
            if height[l] < height[r]:
                l += 1

            # if right is shorter, decrement right to previous height
            else:
                r -= 1

        return maxWater  