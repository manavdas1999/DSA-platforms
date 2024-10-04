
# Using swap sort: Time O(n), Space O(1)
# Note: if no constraint on space, use set to find missing


def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    i = 0
    while(i < len(nums)):
        correctIndex = nums[i]-1
        if(nums[correctIndex] == nums[i]):
            i+=1
        else:
            # swap
            nums[correctIndex], nums[i] = nums[i], nums[correctIndex]
    
    # finding missing
    missing = []
    for i in range(len(nums)):
        if(nums[i] != i+1):
            missing.append(i+1)

    return missing
