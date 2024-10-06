
# Using Two Pointer approach
# Idea: if an array is sorted, lowest value at left end, highest value at right end, 
# moving left to right will always increase the pair sum and moving right to left will decrease it.
# Time: O(n) (if sorted array, if not sorted array, this technique may take O(nLogn) time), Space: O(1)


def twoSum(self, numbers: List[int], target: int) -> List[int]:
    low = 0
    high = len(numbers)-1
    while(low < high):
        pair_sum = numbers[low] + numbers[high]
        if(pair_sum == target):
            return [low+1, high+1]

        # if pair sum is lesser, increase its value my moving low to right
        if(pair_sum < target):
            low += 1
        # if pair sum is greater, decrease its value my moving high to left 
        else:
            high -= 1

    return []
