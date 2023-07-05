from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head.next or not head.next.next: return head

        pointer1 = head
        pointer2 = head.next

        #partir la lista en 2 invertir la segunda parte y mergear
        while pointer2 and pointer2.next:
            pointer1 = pointer1.next
            pointer2 = pointer2.next.next

        current = pointer1.next
        previous = pointer1.next = None


        while current:
            tmp = current.next
            current.next = previous
            previous = current
            current = tmp


        while previous:
            tmp = head.next
            tmp2 = previous.next
            head.next = previous
            previous.next = tmp
            head = tmp
            previous = tmp2

        return head




    def print_list(self, head):
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
        return nodes



List = Solution()

b = ListNode(val = 1)
c = ListNode(val = 2)
d = ListNode(val = 3)
e = ListNode(val = 4)
f = ListNode(val = 5)



b.next = c
c.next = d
d.next = e
e.next = f


print(List.reorderList(b))
print(List.print_list(b))
