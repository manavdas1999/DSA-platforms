
# There can be move variations to this solution
# Time: O(n), Space: O(1)


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Idea is to use a delayed pointer, which will start moving after a certain
        # movements of fast pointer.
        # slow points to one node behind the nth node from end.

        # edge case
        if(head.next is None):
            return None
        
        slow = head
        fast = head
        while(fast.next is not None):
            fast = fast.next
            if(n == 0):
                # slow will not move until the distance b/w fast and slow is n
                slow = slow.next
            else:
                n -= 1

        # edge case 2 - removing head node
        if(n > 0):
            head = head.next
        else: 
            # removing non head node
            slow.next = slow.next.next

        return head
