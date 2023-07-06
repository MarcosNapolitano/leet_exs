class doubly_linked_list:

    def __init__(self):
        self.head = None
        self.tail = None

class Node:

    def __init__(self, data, key):
        self.data = data
        self.key  = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):

        self.list = doubly_linked_list()
        self.index = {}
        self.capacity = capacity

        node = Node("test","test")
        self.list.head = node
        self.index["test"] = node

        current = self.list.head

        for i in range(1,capacity):
            node = Node(f"test+{i}",f"test+{i}")
            self.index[f"test+{i}"] = node
            current.next = node
            node.prev = current
            current = current.next

        self.list.tail = current
    

    def get(self, key: int) -> int:


        if self.index.get(key):  

            if self.list.tail.key == key: return self.list.tail.data

            if self.capacity > 2:

                #une los extremos del nodo cortado
                self.index[key].prev.next = self.index[key].next
                self.index[key].next.prev = self.index[key].prev

                #hace del nodo cortado la cola y lo une al nodo anterior
                self.index[key].prev = self.list.tail
                self.index[key].next = None
                self.list.tail.next = self.index[key]
                self.list.tail = self.index[key]

            else:

                self.list.head = self.list.tail
                self.list.tail = self.index[key]

                self.list.head.next = self.index[key]
                self.index[key].prev = self.list.head

            print(self.index.get(key).data)
            return self.index.get(key).data

        else:
            return -1

        

    def put(self, key: int, value: int) -> None:

        if self.get(key)!=-1:

            self.index[key].data = value

        else:

            new_node = Node(value, key)

            #borramos el par del dict
            print(self.index)
            del self.index[self.list.head.key]
            self.index[key] = new_node


            if self.capacity > 2 :

                #borramos la cabeza
                self.list.head.next.prev = None
                self.list.head = self.list.head.next

                #parcheamos las relaciones
                new_node.prev = self.list.tail
                self.list.tail.prev.next = new_node

                #asignamos la nueva cola
                self.list.tail = new_node
            
            else:

                self.list.head = self.list.tail
                self.list.tail = new_node
                self.list.head.next = new_node
                new_node.prev = self.list.head
                
        
        return



# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(1)



obj.put(2,1)

print(obj.get(2))
obj.put(3,2)

print(obj.get(2))
print(obj.get(3))










