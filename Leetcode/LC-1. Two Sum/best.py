
# Using Dictionary (hashmap)/Hashing: Time O(n), Space O(n)
# Best if space is not a concern

# Naive approach is Time O(n2), nested loops

def twoSum(self, nums: List[int], target: int) -> List[int]:
    nums_dict = dict()
    for i in range(len(nums)):
        partner = target - nums[i] 
        if partner in nums_dict:
            partnerIndex = nums_dict[partner]
            return [i, partnerIndex]
        else:
            nums_dict[nums[i]] = i

    return []
    
