n = int(input())
nums = [int(item) for item in input().split()]
sums = [nums[0]]
for i in range(1, n):
    sums.append(max(nums[i], nums[i] + sums[i-1]))
        
print(max(sums))