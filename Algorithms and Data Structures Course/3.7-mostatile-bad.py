"""# the solution that I had in mind was too complicated
import itertools as it
from typing import Iterable
n = int(input())
permutes = list(it.combinations_with_replacement(list(range(1,n)), 3))

def is_triangle(iter) -> bool:
    if len(iter)==3:
        a = (iter[0] + iter[1]) > iter[2]
        b = (iter[0] + iter[2]) > iter[1]
        c = (iter[1] + iter[2]) > iter[0]
        if a and b and c:
            return True
        else:
            return False
    else: 
        return False
    

# results = []
count = 0
for item in permutes:
    if sum(item) == n and is_triangle(item):
        count += 1
        # results.append(item)
       
# print(results)
# print(is_triangle((4,4,4)))
print(count)"""

count = 0
n = int(input())
for a in range(1, n+1):
    for b in range(a, n-a+1):
        c = n - a - b
        if (a + b > c and c >= b): 
            count += 1
            
print(count)
        