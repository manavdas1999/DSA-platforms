
# Idea: have three pointers prev, curr, next and use them to switch pointers
# Time: O(n), space: O(1)
# Iterative Approach

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      if(head is None or head.next is None):
           return head
      prev = None
      curr = head
      next = curr.next
      while(curr is not None):
          curr.next = prev
          prev = curr
          curr = next
        # do note next can become None 
          if(next is not None):
              next = next.next
      return prev
