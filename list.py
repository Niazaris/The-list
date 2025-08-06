from typing import Any, Iterable

class _Node:
    def __init__(self, current: Any, next = None):
        self.current = current
        self.next = next
    
class List:
    def __init__(self) -> None:
        self._head = None
        self._size = 0
        
    def __iter__(self):
        current = self._head
        while current:
            yield current.current
            current = current.next
        
    def __str__(self) -> str:
        return f"[{', '.join(str(current) for (current) in self)}]"
                
    def append(self, item: Any) -> None:
        new_node = _Node(item)
        if self._head is None:   
            self._head = new_node
        else:    
            current = self._head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1
        
    def insert(self, position: int, item: Any) -> None:
        if not isinstance(position, int):
            raise TypeError("position must be an integer")
        if position < 0:
            position += self._size
        if position < 0 or position > self._size:
            raise IndexError("Index out of range")
        new_node = _Node(item)
        if position == 0:
            new_node.next = self._head
            self._head = new_node
        else:
            current = self._head
            for i in range(position - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self._size += 1
        
    def remove(self, item: Any) -> None:
        current = self._head
        previous = None
        while current:
            if current.current == item:
                if previous:
                    previous.next = current.next
                else:
                    self._head = current.next
                self._size -= 1
                return
            previous = current
            current = current.next
        raise ValueError("Value not found")
        
    def pop(self, position: int = -1) -> Any:
        if not isinstance(position, int):
            raise TypeError("Position must be an integer")
        if self._size == 0:
            raise IndexError("The list is empty")
        if position < 0:
            position += self._size
        if position < 0 or position >= self._size:
            raise IndexError("Index out of range")
        
        current = self._head
        previous = None
        for i in range(position):
            previous = current
            current = current.next
        if previous:
            previous.next = current.next
        else:
            self._head = current.next
        self._size -= 1
        return current.current
        
    def reverse(self) -> None:
        current = self._head
        previous = None
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self._head = previous
        
    def index(self, item: Any, start: int = 0, end: int = None) -> int:
        if not isinstance(start, int):
            raise TypeError("start must be an integer")
        if end is not None and not isinstance(end, int):
            raise TypeError("end must be an integer or None")           
        if end is None:
            end = self._size
        if end < 0:
            end += self._size
        if start < 0:
            start += self._size            
        if start < 0 or start > self._size:
            raise IndexError("start index out of range")
        if end < 0 or end > self._size:
            raise IndexError("start index out of range")
            
        current = self._head
        current_position = 0
        while current:
            if current_position >= start and current_position < end:
                if current.current == item:
                    return current_position
            current = current.next
            current_position += 1
            
    def extend(self, iterable: Iterable[Any]) -> None:
        for item in iterable:
            self.append(item)
            
    def count(self) -> int:
        return self._size
        
    def clear(self) -> None:
        self._head = None
        self._size = 0
        
    def copy(self):
        new_list = List()
        current = self._head
        while current:
            new_list.append(current.current)
            current = current.next
        return new_list
        
    def __getitem__(self, item: int) -> Any:
        if not isinstance(item, int):
            raise TypeError("Item must be an integer")
        if item > 0:
            item += self._size
        if item < 0 or item >= self._size:
            raise IndexError("Index out of range")
        current = self._head
        for i in range(item):
            current = current.next
        return current.current
        
    def __setitem__(self, position: int, item: Any) -> None:
        if not isinstance(position, int):
            raise TypeError("Position must be an integer")
        if item < 0:
            position += self._size
        if position < 0 or position >= self._size:
            raise IndexError("Index out of range")
        current = self._head
        for i in range(position):
            current = current.next
        current.current = item
            
            
if __name__ == '__main__':
    new_list = List()
    new_list.append(2)
    new_list.append(5)
    new_list.append(8)
    new_list.append(17)
    new_list.append(72)
    new_list.append(2)
    new_list.append(554)
    new_list.append(438)
    new_list.append(173)
    new_list.append(2)
    print(new_list)
    new_list[1] = 69
    print(new_list)
    print(new_list.index(2,6,8))
    #new_list.insert(0, 99)
    #new_list.insert(2, 99)
    #print(new_list)
    #new_list.reverse()
    #print(new_list)
    #print(new_list[4])
    #new_list.remove(99)
    #print(new_list)
    #print(new_list.count())
    #print("---------------")
    #print(new_list.pop(1))
    #print(new_list.pop())
    #print(new_list.pop(-2))
    #print(new_list)
    #new_list.clear()
    #print(new_list)