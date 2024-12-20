# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # approach One
        """
        c = 0
        temp = head

        while temp is not None:
            c += 1
            temp = temp.next
        mid = c // 2

        temp = head
        for i in range(mid):
            temp = temp.next
        
        return temp"""

        #approach Two using Fast and slow pointers

        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow



        