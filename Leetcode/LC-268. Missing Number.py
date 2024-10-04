
# Using Swap sort - Time: O(n), Space: O(1), scalable for multiple missing values

# Better approach: Maths, missing = sum of actual - sum of 0-n
# but limited to only one missing value


def missingNumber(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            correctIndex = nums[i]-1
            if nums[i] == 0 or nums[correctIndex] == nums[i] :
                # nums[i] at right place (and also skip 0)
                i+=1
            else:
                nums[correctIndex], nums[i] = nums[i], nums[correctIndex]
        
        # checking for missing
        missing = 0 # by default, assuming 0 is missing
        for i in range(len(nums)):
            if(nums[i] != i+1):
                missing = i+1
                break
        
        return missing
