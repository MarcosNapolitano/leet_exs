# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        current = head.next
        new_list = Node(x = head.val)
        new_list_pointer = new_list

        index = {}

        index[head] = new_list

        while current:
            new_node = Node(x = current.val)
            new_list_pointer.next = new_node
            index[current] = new_node
            current = current.next
            new_list_pointer = new_list_pointer.next

        current, new_list_pointer = head, new_list

        print(index)

        while new_list_pointer:

            if current.random!=None:
                print("hola")
                new_list_pointer.random = index[current.random]
            else:
                new_list_pointer.random = None
            new_list_pointer = new_list_pointer.next
            current = current.next

        return new_list

    def print_list(self, head):
        nodes = []
        nodes_ran = []
        while head:
            nodes.append(head.val)
            if not head.random:
                nodes_ran.append(head.random)
            else:
                nodes_ran.append(head.random.val)
            head = head.next
        return nodes, nodes_ran


List = Solution()

b = Node(x = 7)
c = Node(x = 13)
d = Node(x = 11)
e = Node(x = 10)
f = Node(x = 1)

b.next = c
c.next = d
d.next = e 
e.next = f 

b.random = None 
c.random = b 
d.random = f 
e.random = d 
f.random = b

print(List.print_list(List.copyRandomList(b)))



