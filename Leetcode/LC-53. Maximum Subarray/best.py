
# Idea: Kadane's algorithm
# time: O(n), space: O(1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Greedy approach - Kadane's algorithm
        currSum = 0
        maxSum = nums[0]
        for i in range(len(nums)):
            currSum += nums[i]
            maxSum = max(maxSum, currSum)
            # idea is that adding a negative sum to next no. will only reduce it
            # and hence does not contribute to further maximizing of sum
            # so we reset the sum to 0 indicating a new subarray
            # eg: -2, 1, 8;  -2 + 1 = -1 + 8 = 7;  0 + 1 + 8 = 9(greater)
            if(currSum < 0):
                currSum = 0
        
        return maxSum
        
