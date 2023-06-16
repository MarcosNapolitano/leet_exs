# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.tail = None
    
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
    def addTwoNumbers(self, l1 = ListNode(0), l2 = ListNode(0)):

        def createNumber(l):
            lista = [str(l.val)]
            current = l.next
            while current != None:
                lista.append(str(current.val))
                current = current.next
            return lista
        
        numero1 = "".join(list(reversed(createNumber(l1))))
        numero2 = "".join(list(reversed(createNumber(l2))))

        result = str(eval(numero1+"+"+numero2))
        result = list(reversed([*result]))

        result_list = ListNode(int(result[0]))

        if len(result)==1:
            return result_list
        else:
            for i in range(len(result)):
                if i==0:
                    continue

                result_list.add(int(result[i]))
                
            return result_list
                






Lista1 = ListNode(2)

print(Lista1.add(4))
Lista1.add(3)

print(Lista1.next.next)


Nodo1 = ListNode(5)
Nodo2 = ListNode(6)
Nodo3 = ListNode(4)

Nodo1.next = Nodo2
Nodo1.next.next = Nodo3

Lista2 = Nodo1

Solucion = Solution()

print(Solucion.addTwoNumbers(l1 = Lista1, l2 = Lista2))

