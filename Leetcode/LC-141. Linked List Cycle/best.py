
# Idea: Floyd's cycle detection algorithm
# Time: O(n), space: O(1)
# Other method could be using a set of nodes to check for duplicate, space: O(n)
def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Fast and slow pointer technique
        slow = head
        fast = head
        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next

            # cycle found, checking it last because 1st node will always be same for both
            if(slow == fast):
                return True
        # list terminated, no cycle
        return False
