import copy
from itertools import combinations

notneeded = input()
Set = [int(item) for item in input().split()]
n = len(Set)

combs = []
for i in range(1,n):
    for item in combinations(Set, i):
        combs.append(list(item))

minimum = sumset = sum(Set)
for item in combs:
    mini_sum = abs(sumset - 2*sum(item))
    if( mini_sum < minimum):
        minimum = copy.deepcopy(mini_sum)

print(minimum)
# print(combs)