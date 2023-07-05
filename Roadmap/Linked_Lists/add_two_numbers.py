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