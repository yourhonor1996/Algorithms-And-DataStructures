notneeded = input()
nums = [int(item) for item in input().split()]
# nums = [1,3,1,2,3]
# nums = [5,7,3,3,7,5,3]
#sort the numbers
nums.sort()

time = 0
count = 0
for item in nums:
    if(item > time):
        count += 1
        time += 1

print (count)