import sys
sys.setrecursionlimit(2000)

not_important = input()
input_arr = [int(item) for item in input().split()]

def insertionSortRecursive(arr,n):
    # base case
    if n<=1:
        return
      
    # Sort first n-1 elements
    insertionSortRecursive(arr,n-1)
    '''Insert last element at its correct position
        in sorted array.'''
    last = arr[n-1]
    j = n-2
      
    while (j>=0 and arr[j]>last):
        arr[j+1] = arr[j]
        j = j-1
  
    arr[j+1]=last

n = len(input_arr)
insertionSortRecursive(input_arr, n)
print(*input_arr)