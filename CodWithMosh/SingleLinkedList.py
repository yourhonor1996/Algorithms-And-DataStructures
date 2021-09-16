from typing import Type


class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next: LinkedList.Node = None

        def __repr__(self) -> str:
            return f"*{self.data}*"

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
        while current != None:
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
        # if k <= 0 or k > self.size:
        #     return
        if k == 1:
            return self.last

        # place the second pointer
        for i in range(k - 1):
            second = second.next
            if second is None:
                raise ValueError(
                    "The number K shouldn't be greateer than the size of the list."
                )
        # go to the end until your second pointer reaches the end
        while True:
            if second == self.last:
                return first
            first = first.next
            second = second.next


ll = LinkedList()
ll.add_last(1)
ll.add_last(2)
ll.add_last(3)
ll.add_last(4)
ll.add_last(5)
ll.add_last(6)
# print(ll.index_of(36))
# print(ll)
# ll.delete_first()
# print(ll)
# print(ll.to_array())
# for item in ll.generator_reversed():
#     print(item)
# print(ll.generator_reversed())
k = 9
print(ll)
print(ll.get_Kth_node_from_end(k))
ll.reverse()
print(ll)
# print(ll)
print(ll.get_Kth_node_from_end(k))
