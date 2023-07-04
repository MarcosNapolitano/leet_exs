from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1: return list2

        if not list2: return list1

        if not list1 and not list2: return None

        current_1 = list1
        current_2 = list2
        list3 = None
        current = None

        while current_2 or current_1:

            if not current_1: 
                current.next = current_2
                current = current.next
                current_2 = current_2.next
                continue

            if not current_2: 
                current.next = current_1
                current = current.next
                current_1 = current_1.next
                continue

            if current_1.val <= current_2.val:

                if not list3: 
                    list3 = current_1
                    current = list3
                    current_1 = current_1.next
                    continue

                current.next = current_1
                current_1 = current_1.next

            else:

                if not list3: 
                    list3 = current_2
                    current = list3
                    current_2 = current_2.next

                    continue

                current.next = current_2
                current_2 = current_2.next

            current = current.next




        #tengo que hacer que retorne la lista en la que trabaja q siempre sea la misma
        
        return list3.next.next.next.val



        


List = Solution()

a = ListNode(val = 5)


b = ListNode(val = 1)
c = ListNode(val = 2)
d = ListNode(val = 4)

b.next = c
c.next = d

print(List.mergeTwoLists(a, b))