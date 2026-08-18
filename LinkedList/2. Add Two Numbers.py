# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # # My first version
        # quotient = remainder = 0
        # res = ListNode(remainder)
        # curr = res

        # while l1 or l2:
        #     if l1 and l2:
        #         sum_up = l1.val + l2.val + quotient
        #         l1 = l1.next
        #         l2 = l2.next
        #     else:
        #         if l1:
        #             sum_up = l1.val + quotient
        #             l1 = l1.next

        #         elif l2:
        #             sum_up = l2.val + quotient
        #             l2 = l2.next
        #     quotient, remainder = divmod(sum_up,10)

        #     curr.next = ListNode(remainder)
        #     curr = curr.next

        # if quotient:
        #     curr.next = ListNode(quotient)
        #     curr = curr.next
        
        # return res.next


        # Simplify 
        quotient = remainder = 0
        res = ListNode(remainder)
        curr = res

        while l1 or l2 or quotient:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            sum_up = v1 + v2 + quotient
            quotient, remainder = divmod(sum_up,10)
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            curr.next = ListNode(remainder)
            curr = curr.next
        
        return res.nextx