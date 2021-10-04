from copy import deepcopy
q = int(input())
nums = []
for i in range(q):
    nums.append([int(item) for item in input().split()])

all = [[None for i in range(2002)] for j in range(2002)]
# all = [[None]*3]*3

max_n = 2002
for i in range(max_n):
    for j in range(i+1):
        if(j == 0 or i == j):
            # all[i].append(1)
            all[i][j] = 1
        else:
            all[i][j] = int((all[i-1][j] + all[i-1][j-1]) % int(1e9 + 7))

for num in nums:
    if (num[0] < num[1]):
        print(0)
        continue
    print(all[num[0]][num[1]])