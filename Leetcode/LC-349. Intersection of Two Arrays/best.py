
# Trick: having all values as set reduces the time to search values and processing duplicates.
# Time: O(n), Space: O(1) (assuming only auxiliary space is counted)

def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    commons = set()
    nums1_set = set(nums1)
    nums2_set = set(nums2)
    for i in nums1_set:
        if i in nums2_set:
            commons.add(i)
    return commons
