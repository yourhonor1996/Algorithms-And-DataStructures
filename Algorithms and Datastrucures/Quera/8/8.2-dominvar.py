from copy import deepcopy
n = int(input())


def domino(k:int):
    if k in [0, 1]:
        return 1
    fn2 = 1
    fn1 = 1
    fn = 0
    for i in range(k-1):
        fn = fn1 + fn2
        fn2 = deepcopy(fn1)
        fn1 = deepcopy(fn)
    return fn
        
print(domino(n) % int(1e9 + 7))