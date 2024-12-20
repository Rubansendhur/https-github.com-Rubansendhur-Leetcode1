# Definition for singly-linked list.
# class ListNode:
#     def _init_(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        n=0
        m=0
        temp=headA
        while temp is not None:
            m=m+1
            temp=temp.next
        temp=headB
        while temp is not None:
            n=n+1
            temp=temp.next
        diff=0
        hA=headA
        hB=headB
        if m>n:
            diff=m-n
            while diff>0:
                hA=hA.next
                diff=diff-1
        elif n>m:
            diff=n-m
            while diff>0:
                hB=hB.next
                diff=diff-1
        while (hA is not None and hB  is not None):
            if hA==hB:
                return hA
            hA=hA.next
            hB=hB.next