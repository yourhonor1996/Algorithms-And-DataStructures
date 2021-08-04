import sys
import copy
sys.setrecursionlimit(100000)

def ntayi(k, i):
    result = []
    if i==1:
        result.append(list('1' * k)) 
    else: 
        last = ntayi(k, i-1)
        for j in range(k):
            last[k-i+1] = str(int(last[k-i+1]) + 1)
            result.append(last)
            # return last

def ntayi2(k):
    results = []
    start = [1]*k
    results.append(copy.deepcopy(start))
    for i in range(k-1, -1, -1):
        for j in range(k-1):
            start[i] += 1
            results.append(copy.deepcopy(start)) 
    return results
print(ntayi2(3))
# print(list('1' * 5))