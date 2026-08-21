# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        preleft, curr = dummy,head
        

        for i in range(left -1):
            preleft,curr = curr,curr.next
        
        pre = None
        for i in range(right-left+1):
            temp = curr.next
            curr.next = pre
            pre,curr = curr,temp 

        preleft.next.next = curr
        preleft.next = pre

        return dummy.next
        #双指针，一个停在反转前锚定，翻转好后链接
