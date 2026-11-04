# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:

        # merge sort 的原理
        if not head:
            return head
        if not head.next:
            return head
        dummy1 = ListNode(0)
        curr = dummy1
        dummy1.next = head
        count = 0

        while curr.next:
            curr = curr.next 
            count +=1
        
        mid = count // 2

        fast = dummy1
        while mid:
            fast = fast.next
            mid-=1
    
        secondhead = fast.next

        # !!! 记着要断开前一段的结尾，前一个的结尾是fast， 所以把fast.next 原值存好后，fast.next 要断开连到none
        fast.next = None
        
        
        first = self.sortList(head)
        second = self.sortList(secondhead)


        def merge(list1,list2):
            curr1 = list1
            curr2 = list2
            
            dummy = ListNode(0)
            curr = dummy 

            while curr1 and curr2:
                if curr1.val <= curr2.val:
                    curr.next = curr1
                    curr = curr.next
                    curr1 = curr1.next
                else:
                    curr.next = curr2
                    curr = curr.next 
                    curr2 = curr2.next
            
            if curr1:
                curr.next = curr1
            if curr2:
                curr.next = curr2
            return dummy.next
            

        return merge(first,second)

        # time complexity O(nlogn)
        # Space complexity O (logn)： 每次recursive 一层只要不到返回的时候这些stack都同时存在 层数是logn

        # gap： 每次切两段的时候都要想一下第一段的末尾是不是断联了






        
        
        