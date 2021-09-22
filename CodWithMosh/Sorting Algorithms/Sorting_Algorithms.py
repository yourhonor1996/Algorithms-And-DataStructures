class Sort(object):
    def __init__(self, array: list) -> None:
        self.array = array

    @staticmethod
    def swap(lis: list, index1: int, index2: int):
        temp = lis[index1]
        lis[index1] = lis[index2]
        lis[index2] = temp

    @staticmethod
    def minimum(arr: list, start: int = None, finish: int = None):
        length = len(arr)
        start = start or 0
        finish = finish or length

        minimum = arr[start]
        for i in range(start + 1, finish):
            curr = arr[i]
            if curr < minimum:
                minimum == curr

        return minimum

    @staticmethod
    def shift(arr: list, index: int):
        temp = arr[index]
        arr[index] = arr[index - 1]
        return temp

    def bubble_sort(self):
        length = len(self.array)
        for i in range(length):
            is_sorted = True
            for i in range(1, length - i):
                if self.array[i] < self.array[i - 1]:
                    Sort.swap(self.array, i, i - 1)
                    is_sorted = False
            if is_sorted:
                break
        return self.array

    def selection_sort(self):
        length = len(self.array)

        for i in range(length):
            minimum = self.array[i]
            min_index = i
            for j in range(i + 1, length):
                curr = self.array[j]
                if curr < minimum:
                    minimum = curr
                    min_index = j

            Sort.swap(self.array, i, min_index)
        return self.array

    def insertion_sort(self):
        length = len(self.array)
        # result = []
        for i in range(1, length):
            curr = self.array[i]
            j = i
            while curr < self.array[j - 1]:
                Sort.shift(self.array, j)
                j -= 1
                if j == 0:
                    break
            self.array[j] = curr
        return self.array

    def merge_sort(self):
        pass

    def quick_sort(self):
        pass


s1 = Sort([9, 8, 7, 6, 5, 4])
s2 = Sort([1, -2])
# print(s1.bubble_sort())
# print(s2.bubble_sort())
# print(s1.sVCVselection_sort())
print(s1.insertion_sort())
