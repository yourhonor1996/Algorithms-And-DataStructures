import sys 
sys.setrecursionlimit(10**6)

number = int(input())
# number = 10


def find_fn(n: int):
    if(n == 0):
        return 5
    if(n % 2 == 0):
        return find_fn(n-1) - 21
    if(n % 2 == 1):
        return find_fn(n-1)**2

print(find_fn(number))
