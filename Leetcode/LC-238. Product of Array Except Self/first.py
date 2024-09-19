
# Idea: prefix and postfix product
# on the result list performing prefix product and then postfix product
# TIME: O(n), SPACE: O(n) 

def productExceptSelf(self, nums: List[int]) -> List[int]:
      # 2nd best approach with extra space
      res = [1] * len(nums) # creating a list of size len(nums) and initialized with 1
      # performing prefix product on result from nums
      pre = 1
      for i in range(len(nums)):
          res[i] = res[i] * pre
          pre = pre * nums[i]

      # performing postfix product on result from nums
      post = 1
      for i in range(len(nums)-1, -1, -1):
          res[i] = res[i] * post
          post = post * nums[i]
      
      return res
