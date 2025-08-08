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
        return f"[{', '.join(repr(current) for current in self)}]"
        
    def __repr__(self):
        return self._str__()
                
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
            
        if position > self._size:
            position = self._size
        if position < 0:
            position = 0
            
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
            
        current = self._head
        current_position = 0
        while current:
            if current_position >= start and current_position < end:
                if current.current == item:
                    return current_position
            current = current.next
            current_position += 1
        
        raise ValueError("Value in not in list")
            
    def extend(self, iterable: Iterable[Any]) -> None:
        if not isinstance(iterable, Iterable):
            raise TypeError("Item must be an iterable")
        for item in iterable:
            self.append(item)
            
    def count(self, item: Any) -> int:
        count = 0
        current = self._head
        while current:
            if current.current == item:
                count += 1
            current = current.next
        return count
        
    def clear(self) -> None:
        self._head = None
        self._size = 0
        
    def copy(self) -> "List":
        new_list = List()
        current = self._head
        while current:
            new_list.append(current.current)
            current = current.next
        return new_list
        
    def __len__(self) -> int:
        return self._size
        
    def __getitem__(self, item: "int | slice") -> Any:
        if isinstance(item, slice):
            start, end, step = item.indices(self._size)
            result = List()
            current = self._head
            current_position = 0
            
            if step == 0:
                raise ValueError("Slice step cannot be zero")
                
            while current:
                if current_position >= start and current_position < end:
                    if (current_position - start) % step == 0:
                        result.append(current.current)
                elif current_position >= end:
                    break
                current = current.next
                current_position += 1
             
            return result
                
        elif isinstance(item, int):
            if item < 0:
                item += self._size                
            if item < 0 or item >= self._size:
                raise IndexError("Index out of range")
            current = self._head
            
            for i in range(item):
                current = current.next
            return current.current
        else:
            raise TypeError("Item must be int or slice")
        
    def __setitem__(self, position: int, item: Any) -> None:
        if not isinstance(position, int):
            raise TypeError("Position must be an integer")
        if position < 0:
            position += self._size
        if position < 0 or position >= self._size:
            raise IndexError("Index out of range")
        current = self._head
        
        for i in range(position):
            current = current.next
        current.current = item
        
    def __delitem__(self, position: int) -> None:
        if not isinstance(position, int):
            raise TypeError("Position must be an Integer")
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