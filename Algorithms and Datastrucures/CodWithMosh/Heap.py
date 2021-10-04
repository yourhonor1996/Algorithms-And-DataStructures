from typing import Union


class Heap(object):
    def __init__(self) -> None:
        self.data = []

    def __repr__(self) -> str:
        return str(self.data)

    @property
    def is_empty(self) -> bool:
        return len(self.data) == 0

    @staticmethod
    def swap_list(lis, index1, index2):
        temp = lis[index1]
        lis[index1] = lis[index2]
        lis[index2] = temp

    @staticmethod
    def parent_i(child_index) -> int:
        return int((child_index - 1) / 2)

    @staticmethod
    def left_i(node_i : int):
        return node_i * 2 + 1

    @staticmethod
    def right_i(node_i : int):
        return node_i * 2 + 2

    def left(self, node_i : int):
        return self.data[Heap.left_i(node_i)]

    def right(self, node_i : int):
        return self.data[Heap.right_i(node_i)]

    def has_left(self, node_i : int):
        return Heap.left_i(node_i) < len(self.data)

    def has_right(self, node_i : int):
        return Heap.right_i(node_i) < len(self.data)

    def larger_child_i(self, node_i : int):
        if not self.has_left(node_i):
            return node_i

        if not self.has_right(node_i):
            return self.left_i(node_i)

        return self.right_i(node_i) if self.right(node_i) >= self.left(node_i) else self.left_i(node_i)

    def is_valid_parent(self, node_i : int):
        if not self.has_left(node_i):
            return True

        if not self.has_right(node_i):
            return self.data[node_i] >= self.left(node_i)

        return self.data[node_i] >= max(self.left(node_i), self.right(node_i))

    def bubble_up(self):
        index = len(self.data) - 1
        parent_i = Heap.parent_i(index)

        while index > 0 and self.data[index] > self.data[parent_i]:
            Heap.swap_list(self.data, index, parent_i)
            index = parent_i
            parent_i = Heap.parent_i(index)

        return index

    def bubble_down(self):
        index = 0
        size = len(self.data)

        while index < size and not self.is_valid_parent(index):
            larger_child_i = self.larger_child_i(index)
            Heap.swap_list(self.data, index, larger_child_i)
            index = larger_child_i

        return index

    def insert(self, value):
        self.data.append(value)
        index = self.bubble_up()

        return index

    def remove(self):
        if self.is_empty:
            return

        if len(self.data) == 1:
            return self.data.pop(0)

        removed_item = self.data.pop(0)
        self.data.insert(0, self.data.pop())
        self.bubble_down()
        return removed_item

    @staticmethod
    def somefunc(someparam: Union["Heap", list]):
        print(someparam)

    def heap_sort(self):
        pass

    @staticmethod
    def heap_sort_array(arr):
        heap = Heap()
        for item in arr:
            heap.insert(item)
        for i in range(len(arr)):
            arr[i] = heap.remove()
        return arr

    def heap_sort_self(self):
        heap = Heap()
        results = []
        for item in self.data:
            heap.insert(item)
        for i in range(len(self.data)):
            results.append(heap.remove())
        return results


class PriorityQueue(object):
    def __init__(self) -> None:
        self.heap = Heap()

    def __repr__(self) -> str:
        return str(self.heap.data)

    def add(self, data):
        self.heap.insert(data)

    def remove(self, data):
        return self.heap.remove()


heap = Heap()
heap.insert(10)
heap.insert(5)
heap.insert(17)
heap.insert(4)
heap.insert(22)
heap.insert(22)
heap.insert(22)
# print(heap)
# heap.a
# # for i in range(len(heap.data)):
# #     heap.remove()

a = [3, 6, 26, 1, -4, -63]
# # print(heap.remove())
# print(heap.remove())
# print(heap.remove())
# print(heap.remove())
# print(heap.heap_sort())
# print(Heap.heap_sort(a))
# Heap.heap_sort(a)
