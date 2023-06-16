# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

    def add(self, node):
        newNode = ListNode(node)
        if not self.next:
            self.next = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

        return node


class Solution:
    def mergeTwoLists(self, list1, list2):

        if not list2: return list1

        currentNode1 = list1
        currentNode2 = list2

        while currentNode1.val<currentNode2.val:
            currentNode1 = currentNode1.next

        restof1 = currentNode1.next
        currentNode2.next = None
        currentNode1.next = currentNode2
        currentNode1.next.next = restof1
        list2 = list2.next

        self.mergeTwoLists(currentNode1,list2)


Lista1 = ListNode(1)

Lista1.add(2)
Lista1.add(4)

Nodo1 = ListNode(1)
Nodo2 = ListNode(3)
Nodo3 = ListNode(4)

Nodo1.next = Nodo2
Nodo1.next.next = Nodo3

Lista2 = Nodo1

solucion = Solution()

print(solucion.mergeTwoLists(Lista1, Lista2))




            

            
