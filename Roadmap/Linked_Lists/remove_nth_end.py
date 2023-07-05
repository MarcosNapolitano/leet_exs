from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        previous = head
        current  = head.next
        next_n = current

        if not next_n.next:
            if n == 1:
                previous.next = None
                return previous
            elif n == 2:
                previous.next = None
                return current

        while n>0 and next_n:
            next_n = next_n.next
            n-=1


        #esto quiere decir que hay que remover la cabeza
        if n>0: return current

        while next_n:
            previous = current
            current  = current.next
            next_n = next_n.next


        previous.next = current.next
        
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





b.next = c
c.next = d


print(List.print_list(List.removeNthFromEnd(b,2)))
