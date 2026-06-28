class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visit_lst = []
        while head is not None:
            if head in visit_lst:
                return True
            else:
                visit_lst.append(head)
                head = head.next
        return False
        