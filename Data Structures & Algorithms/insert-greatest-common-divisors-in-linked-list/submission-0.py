# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a,b):
            while b > 0:
                temp = a
                a =b
                b = temp %b
            return a
        cur = head
        while cur.next:
            n1 = cur.val
            n2 = cur.next.val
            cur.next = ListNode(gcd(n1,n2), cur.next)
            cur = cur.next.next
        return head
