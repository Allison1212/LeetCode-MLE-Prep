# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # My version 
        dummy = ListNode(0)
        curr = dummy 
        while list1 or list2:
            if list1 and list2:
                if list1.val <= list2.val:
                    new_node = ListNode(list1.val)
                    list1 = list1.next
                else:
                    new_node = ListNode(list2.val)
                    list2 = list2.next
            elif list1:
                new_node = ListNode(list1.val)
                list1 = list1.next
            else:
                new_node = ListNode(list2.val)
                list2 = list2.next
            curr.next = new_node
            curr = curr.next
            
    

        return dummy.next

        # Try to improve
        dummy = ListNode(0)
        curr = dummy 
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = ListNode(list1.val)
                list1 = list1.next
            else:
                curr.next = ListNode(list2.val)
                list2 = list2.next
            
            curr = curr.next 

        if list1: curr.next = list1
        if list2: curr.next = list2

        return dummy.next

        # Optimal
        dummy = ListNode(0)
        curr = dummy 
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            
            curr = curr.next 

        curr.next = list1 if list1 else list2

        return dummy.next
# Time complexity: O(n+m) where n and m are the lengths of the two lists
# Space complexity: O(1) since we are not using any extra space for the new list, we are just rearranging the pointers of the existing nodes.