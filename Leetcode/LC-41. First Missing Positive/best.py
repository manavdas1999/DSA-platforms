
# Using swap sort: Time: O(n), Space: O(1)
# NOTE: There can be other ways of solving it by removing non positive and length greater values by some place holders and then checking


def firstMissingPositive(self, nums: List[int]) -> int:
    i = 0
    while(i < len(nums)):
        # we are ignoring non-positive values and values greater than n as they are not of our concern
        is_valid_value = nums[i] > 0 and nums[i] <= len(nums)
        correctIndex = nums[i]-1
        # if value is non-positive or greater than length, simply skip them
        # also skip if value at right position
        if((not is_valid_value) or nums[correctIndex] == nums[i]):
            i += 1
        else:
            # swap
            nums[correctIndex], nums[i] = nums[i], nums[correctIndex]

    # finding first missing
    for i in range(len(nums)):
        if( nums[i] != i+1):
            return i+1

    # n+1 is missing if no other is missing
    return len(nums) + 1 
