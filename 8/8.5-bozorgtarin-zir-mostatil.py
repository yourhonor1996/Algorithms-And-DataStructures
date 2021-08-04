from math import inf
n, m = [int(item) for item in input().split()]
jadval = []
# jadval = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# jadval = [[-3,4,1],[5,7,-1],[-10,-11,-100]]

for i in range(n):
    jadval.append([int(item) for item in input().split()])
    
    
maximum = -inf
for i in range(n):
    for j in range(i, n):
        nums = [sum([row[p] for row in jadval[i:j+1]]) for p in range(m)]
        sums = [nums[0]]
        for c in range(1, len(nums)):
            sums.append(max(nums[c], nums[c] + sums[c-1]))
        maximum = max(maximum, max(sums))
        
print(maximum)