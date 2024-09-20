
# Time: O(n+m), space: O(1)

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # This idea of brilliant, created a new list node(dummy) as head so that we can avoid the
        # issue of handling the head done

        # new head
        mergedHead = ListNode()
        # tail will help in connection and traversal
        tail = mergedHead

        l1 = list1
        l2 = list2
        while(l1 is not None and l2 is not None):
            if(l1.val <= l2.val):
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            
            tail = tail.next
        
        # if any list is remaining
        if(l1 is not None):
            tail.next = l1
        if(l2 is not None):
            tail.next = l2
        
        # as mergeHead was initially a dummy node
        mergedHead = mergedHead.next
        return mergedHead
