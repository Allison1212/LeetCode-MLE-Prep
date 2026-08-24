# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # # First version 
        # if head == None or not head.next:
        #     return head
        # idx_dict = {}
        # dummy = ListNode(0)
        # dummy.next = head
        # curr = dummy.next
        # idx = 0
        # while curr:
        #     idx_dict[idx] = curr
        #     curr = curr.next
        #     idx +=1

        
        # k = k % (idx)
        # if k == 0:
        #     return head

        # temp_head = dummy.next

        # dummy.next = idx_dict[idx-k]
        # idx_dict[idx-k-1].next = None
        # idx_dict[idx-1].next = temp_head

        # return dummy.next 


        # Simplify space complexity 
        if head == None or not head.next:
            return head

        length = 1
        old_tail = new_tail = head

        while old_tail.next:
            old_tail = old_tail.next
            length+=1
        
        k = k % length
        if k == 0:
            return head 
        
        for i in range(length-k-1):
            new_tail = new_tail.next
        
        old_tail.next = head
        new_head = new_tail.next
        new_tail.next = None

        return new_head
        # 做题前要先想清楚boundary case 再动笔，把所有的boundary想清楚
        # 先看一下variable的range

        
        