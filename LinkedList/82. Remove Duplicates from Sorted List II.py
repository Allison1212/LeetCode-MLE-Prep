# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        curr = dummy.next


        while curr:
            if curr.next:
                if curr.val == curr.next.val:
                    while curr.next and curr.val == curr.next.val:
                        curr = curr.next
                    curr = curr.next
                    pre.next = curr
                else:
                    pre,curr = curr,curr.next
            else:
                curr = curr.next
        
        return dummy.next
        