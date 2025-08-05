class Node:
    def __init__(self, current, next = None):
        self.current = current
        self.next = next
    
class List:
    def __init__(self):
        self.head = None
        
    def append(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            
        
    def get(self, value):
        current = self.head
        count = 0
        while value is not None:
            if count == value:
                return current
            count += 1
            current = current.next
            
            
    
new_list = List()
new_list.append(2)
new_list.append(5)
new_list.append(8)
new_list.append(17)
new_list.get(2)
item = new_list.get(2)
print(item.current)
