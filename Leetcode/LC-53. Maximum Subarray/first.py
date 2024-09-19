
# Idea: Loop through values finding sum for each subarray(n2) and keep checking with maxSum
# COMPLEXITY: 
# time : O(n2), space: O(1)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # basic approach

        maxSum = -100000
        for i in range(len(nums)):
            currSum = 0
            for j in range(i, len(nums)):
                currSum += nums[j]
                maxSum = max(maxSum, currSum)
        
        return maxSum
