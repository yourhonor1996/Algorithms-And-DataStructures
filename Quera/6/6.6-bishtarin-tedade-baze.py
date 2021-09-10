n = int(input())
left = []
right = []
all_nums = [int(item) for item in input().split()]
for i, number in enumerate(all_nums):
    if(i % 2 == 0):
        left.append(all_nums[i])
        right.append(all_nums[i+1])

zipped_list = zip(right, left)
sorted_pairs = sorted(zipped_list)

tuples = zip(*sorted_pairs)
right, left = [list(item) for item in tuples]      

lastR = -1
count = 0
for i, r in enumerate(right):
    l = left[i]
    if lastR <= l:
        lastR = r
        count += 1
    

print(count)