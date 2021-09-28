from typing import Union

class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next: LinkedList.Node = None

        def __repr__(self) -> str:
            return f"'{self.data}'"

        def __eq__(self, other: 'LinkedList.Node') -> bool:
            return self.data == other.data

    def __init__(self) -> None:
        self.first: LinkedList.Node = None
        self.last: LinkedList.Node = None
        self.__some = None
        self.size = 0

    def add_last(self, data):
        new_node = LinkedList.Node(data)
        if self.is_empty:
            self.first = self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.size += 1

    def add_first(self, data):
        new_node = LinkedList.Node(data)
        if self.is_empty:
            self.first = self.last = new_node
        else:
            new_node.next = self.first
            self.first = new_node
        self.size += 1

    def delete_first(self):
        if not self.is_empty:
            first = self.first
            second = self.first.next
            first.next = None
            del self.first
            self.first = second
            self.size -= 1
        else:
            return -1

    def contains(self, data):
        return self.index_of(data) != -1

    def index_of(self, data):
        for i, item in self.generator():
            if item.data == data:
                return i
        return -1

    @property
    def is_empty(self):
        return self.first is None

    def __repr__(self) -> str:
        results = []
        for item in self.generator():
            results.append(item)
        return str(results)

    def generator(self):
        index = 0
        current = self.first
        while not current is None:
            yield (index, current)
            current = current.next
            index += 1

    def to_array(self):
        results = []
        for i, item in self.generator():
            results.append(item.data)
        return results

    def reverse(self):
        if self.is_empty:
            return
        previous = self.first
        current = previous.next
        next_item = current.next
        i = 1
        while True:
            current.next = previous
            if next_item is None:
                break
            previous = current
            current = next_item
            next_item = next_item.next

        last = self.last
        self.first.next = None
        self.last = self.first
        self.first = last

    def get_Kth_node_from_end(self, k):
        first = self.first
        second = first

        if k == 1:
            return self.last

        # place the second pointer
        for i in range(k - 1):
            second = second.next
            if second is None:
                raise ValueError("The number K shouldn't be greateer than the size of the list.")

        # go to the end until your second pointer reaches the end
        while True:
            if second == self.last:
                return first
            first = first.next
            second = second.next

    def addlast_if_nonexistant(self, data) -> Union["LinkedList.Node", None]:
        new_node = LinkedList.Node(data)
        if self.is_empty:
            self.first = self.last = new_node
            self.size += 1
            return new_node
        else:
            for i, node in self.generator():
                if node.data == data:
                    return None
                if node.next is None:
                    node.next = self.last = new_node
                    self.size += 1
                    return new_node

    def pop(self, data):
        for i, node in self.generator():
            if self.is_empty:
                return
            else:
                if self.size == 1:
                    if not node.data == data:
                        return
                    self.first = self.last = None
                    # self.size -= 1
                    return node
                    
                elif self.first.data == data:
                    deleted = self.first
                    self.first = deleted.next
                    # self.size -= 1
                    return deleted
                    
                elif (not node.next is None) and (node.next.data == data):
                    deleted = node.next
                    if self.last == deleted:
                        self.last = node
                        
                    node.next = deleted.next
                    # self.size -= 1
                    return deleted
                self.size -= 1
                
            


# link = LinkedList()
# link.add_last(1)
# link.add_last(2)
# # link.add_last(3)
# # link.add_last(5)


# link.pop(1)
# # link.pop(1)
# # link.pop(2)
# # link.pop(2)
# print('done')