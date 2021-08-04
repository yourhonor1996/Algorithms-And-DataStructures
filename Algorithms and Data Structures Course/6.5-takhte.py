n, c = [int(item) for item in input().split()]
nums = [int(item) for item in input().split()]

nums.sort(reverse= True)

for item in nums:
    d= min(c, max(0, item - c))
    c -= d
    
print(c)
