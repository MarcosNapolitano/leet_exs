from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head = None) -> Optional[ListNode]:

        if not head:
            return None

        if not head.next:
            return head

        previous = head
        current = head.next
        previous.next = None

        while current.next:

            tmp = current.next
            current.next = previous
            previous = current
            current = tmp


        current.next = previous

        return current





List = Solution()

a = ListNode()
b = ListNode(val = 1)
c = ListNode(val = 2)
d = ListNode(val = 3)


a.next = b
b.next = c
c.next = d

print(List.reverseList(a))