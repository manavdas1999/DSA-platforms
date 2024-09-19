
# There can be many ways to solve it, using frequencyMap(dictionary), etc
# This logic is cyclic sort
#  time: O(n), space: O(1), NOTE: this changes the list which is not allowed for leetcode


def findDuplicate(self, nums: List[int]) -> int:
      # idea of cyclic sort - array pf [1, n]
      # sort the array by moving the right value to its right place
      # if not found right place then thats the duplicate
      duplicate = 0
      i=0
      while i < len(nums):
          correctIndex = nums[i]-1 # 1-indexed
          # if nums[i] is not at its right place i.e i+1 index
          if(i != correctIndex):
              # if correctIndex is already occupied with correct value 
              # then we found the duplicate
              if(nums[correctIndex] == nums[i]):
                  return nums[i]
              else:
                  # swapping 
                  nums[correctIndex], nums[i] = nums[i], nums[correctIndex]
          else:
              i+=1
          
      return duplicate
