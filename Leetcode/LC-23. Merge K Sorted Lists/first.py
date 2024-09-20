

# Idea: use the logic of merging 2 sorted lists here
# Complexity: Not so sure
# best way is to use heap(will try it)
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # helper function to merge two sorted lists
        def mergeSortedLists(list1, list2):
            mergedHead = ListNode()
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
            
            if(l1 is not None):
                tail.next = l1
            if(l2 is not None):
                tail.next = l2
            
            mergedHead = mergedHead.next
            return mergedHead
        

        # implementation
        if(len(lists) == 0):
            return None

        newHead = lists[0]
        for other in lists[1:]:
            newHead = mergeSortedLists(newHead, other)
        
        return newHead
