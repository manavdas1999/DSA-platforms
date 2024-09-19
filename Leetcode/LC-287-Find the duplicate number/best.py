
# time: O(n), space: O(1)

def findDuplicate(self, nums: List[int]) -> int:
      # best solution: floyd's cycle detection algorithm(slow and fast pointer)
      # this type of given array can be traversed as an linkedlist
      slow = nums[0] # pointing to head
      fast = nums[0]

      while True:
          slow = nums[slow] # slow = slow.next
          fast = nums[nums[fast]] # fast = fast.next.next
          if(slow == fast):
              # when both pointers match, a cycle is detected
              break
          
      # but to find the starting point of cycle(i.e the dupicate number)
      # we have to reset slow to beginning of list and keep moving
      # both slow and fast to normal pace and they will eventually meet
      slow = nums[0] # reset slow to head
      while slow != fast:
          slow = nums[slow]
          fast = nums[fast]

      return slow    
