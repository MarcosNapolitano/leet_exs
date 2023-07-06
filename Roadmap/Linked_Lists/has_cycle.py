#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: "Optional[ListNode]") -> bool:

        if not head:
            return None

        index = {}

        while head:
            try:
                if index[head]: return True

            except:
                index[head] = head

            head = head.next

        return False