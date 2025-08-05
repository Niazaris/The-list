class Node:
    def __init__(self, current, next = None):
        self.current = current
        self.next = next
    
class List:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def append(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
        else:    
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
            
        
    def get(self, item):
        if item < 0 or item >= self.size:
            raise IndexError("Index out of range")
        current = self.head
        for i in range(item):
            current = current.next
        return current.current
                        
    def len(self) -> int:
        return self.size
            
    def show(self):
        current = self.head
        while current:
            print(current.current, end=" ")
            current = current.next
        
    def insert(self, position: int, item):
        if position < 0 or position > self.size:
            raise IndexError("Index out of range")
        new_node = Node(item)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for i in range(position - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.size += 1
        

            
if __name__ == '__main__':
    new_list = List()
    new_list.append(2)
    new_list.append(5)
    new_list.append(8)
    new_list.append(17)
#    print(new_list.get(1))
    print(new_list.show())
    print(new_list.len())
#    new_list.insert(0, 99)
#    new_list.insert(2, 99)
#    print(new_list.show())
#    print(new_list.len())
