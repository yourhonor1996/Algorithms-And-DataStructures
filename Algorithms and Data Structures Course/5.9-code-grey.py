import sys
sys.setrecursionlimit(10**5)
n = int(input())
def grey(k):
    if k==1:
        return ['0', '1']
    else:
        current = grey(k-1)
        reversed = current[::-1]
        current = ['0' + item for item in current]
        reversed = ['1' + item for item in reversed]
        return [*current, *reversed]
    
result = grey(n)
for item in result:
    print(item)
# print(result)
        