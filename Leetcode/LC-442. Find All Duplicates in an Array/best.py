
# Using Swap Sort: Time: O(n), Space: O(1)

def findDuplicates(self, nums: List[int]) -> List[int]:
    i = 0
    while i < len(nums):
        correctIndex = nums[i]-1
        if(nums[correctIndex] == nums[i]):
            i+=1
        else:
            nums[correctIndex], nums[i] = nums[i], nums[correctIndex]
    
    # finding duplicates
    duplicates = []
    for i in range(len(nums)):
        if nums[i] != i+1:
            duplicates.append(nums[i])
    
    return duplicates
