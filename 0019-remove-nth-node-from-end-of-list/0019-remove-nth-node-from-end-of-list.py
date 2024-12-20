# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        m = 0

        while temp is not None:
            m += 1
            temp = temp.next

        pos = (m-n)+1

        if pos == 1:
            return head.next
        else:
            curr = head
            prev = head

            for i in range(1,pos):
                prev = curr
                curr = curr.next
            prev.next = curr.next

            return head
                


                


        