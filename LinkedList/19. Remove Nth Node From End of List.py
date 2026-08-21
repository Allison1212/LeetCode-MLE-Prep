# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # # My first version
        # count = 0 
        # curr = head
        # idx_map = {}
        # while curr:
        #     count+=1
        #     idx_map[count] = curr
        #     curr = curr.next
        
        # curr = head
        # for i in range(1,count):
        #     if curr.next == idx_map[count-n+1]:
        #         curr.next = idx_map[count-n+2] if count-n+2 <= count else None
        #     curr = curr.next

        # return  head.next if count-n+1 == 1 else head


        # # Refine, but still not perfect
        # count = 0 
        # curr = head
        # idx_map = {}
        # while curr:
        #     count+=1
        #     idx_map[count] = curr
        #     curr = curr.next
        
        # curr = head
        # i = 1
        # while i < count-n:
        #     curr = curr.next
        #     i+=1
        
        # curr.next = idx_map[count-n+2] if count-n+2 <= count else None
        # return  head.next if count-n+1 == 1 else head

        # Optimal: two pointer 
        # 如果说到倒数，中间间隔固定，那大概率就是快慢指针
        dummy = ListNode(0)
        dummy.next = head

        fast = slow = dummy

        for i in range(n+1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return dummy.next
        