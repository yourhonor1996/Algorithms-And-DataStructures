from copy import deepcopy as dc
n,m = [int(item) for item in input().split()]
nums = []
for i in range(n):
    nums.append([int(item) for item in input().split()])
    
dp = [[None for j in range(m)] for i in range(n)]
path = [[None for j in range(m)] for i in range(n)]
path_str = []


dp[n-1][0] = nums[n-1][0]

for i in range(1, m):
    dp[n-1][i] = nums[n-1][i] + dp[n-1][i-1]
    path[n-1][i] = 'R'
for i in range(n-2, -1, -1):
    dp[i][0] = nums[i][0] + dp[i+1][0]
    path[i][0] = 'U'

for i in range(n - 2, -1, -1):
    for j in range(1, m):
        dp[i][j] = nums[i][j] + max(dp[i+1][j] , dp[i][j-1])
        if(dp[i+1][j] > dp[i][j-1]):
            path[i][j] = 'U'
        else:
            path[i][j] = 'R'

i = 0
j = m-1
while True:
    if i == n-1 and j == 1:
        path_str.append('R') 
        break
    if i == n-2 and j == 0:
        path_str.append('U')
        break
    if i ==n-1 and j == 0:
        break
    
    if path[i][j] == 'R':
        path_str.append('R')
        j -= 1
    else:
        path_str.append('U')
        i += 1

    

print(dp[0][m-1])
print(''.join(path_str[::-1]))


# dp[n-1][1] = nums[n-1][1]

# for i in range(n):
#     for j in range(m-1, -1, -1):
#         if (dp[i+1][j] > dp[i][j]):
#             dp[i][j] = dp[i+1][j] + nums[i][j]
#             parent[i][j] = 0 #down
#         else:
#             dp[i][j] = dp[i][j-1] + nums[i][j]
#             parent[i][j] = 1 #left     
        
# current_row = 0
# current_column = m-1
# path = []
# while([current_row, current_column] != [n-1, 0]):
#     if (parent[current_row][current_column] == 0):
#         path.append('U')
#     else:
#         path.append('R')
        



