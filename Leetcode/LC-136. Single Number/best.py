
# Using Bit Manipulation (only way for given constraints)
# Idea: XOR operation (^), Read about XOR operation and its working in python.
# Time: O(n), Space: O(1)

def singleNumber(self, nums: List[int]) -> int:
    unique = nums[0]
    for i in range(1, len(nums)):
        unique = unique ^ nums[i]
    return unique
