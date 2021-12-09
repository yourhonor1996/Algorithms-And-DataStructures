from math import inf

n,m = [int(item) for item in input().split()]
nums = []
for i in range(n):
    nums.append([int(item) for item in input().split()])
    
dp = [[[None, None] for j in range(m)] for i in range(n)]

# initialize the starting point of the algorithm
dp[0][0][0] = dp[0][0][1] = nums[0][0]
# initialize the firs row
for j in range(m):
    if j != 0:
        dp[0][j][0] = dp[0][j-1][0] + nums[0][j]
        dp[0][j][1] = inf        
# initialize the firs column and the last column 
# for i in range(n):
#     if i != 0:
#         dp[i][0][0] = inf
    # dp[i][m-1][1] = inf


for i in range(1, n):
    # from left to right
    for j in range(m):
        if j == 0:
            dp[i][j][0] = min(dp[i-1][j][0], dp[i-1][j][1]) + nums[i][j]
        else:
            dp[i][j][0] = min(dp[i][j-1][0], dp[i-1][j][0], dp[i-1][j][1]) + nums[i][j]
    # from right to left
    # for j in range(m-2, -1, -1):
    #     dp[i][j][1] = min(dp[i][j+1][1], dp[i-1][j][0], dp[i-1][j][1]) + nums[i][j]
    for j in range(m-1, -1, -1):
        if j == m-1:
            dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][1]) + nums[i][j]
        else:
            dp[i][j][1] = min(dp[i][j+1][1], dp[i-1][j][0], dp[i-1][j][1]) + nums[i][j]

print(dp[n-1][m-1][0])              
# for i in range(n):
#     for j in range(m):
        
























# # not right 
# from math import inf
# from copy import deepcopy as dc
# n,m = [int(item) for item in input().split()]
# nums = []
# for i in range(n):
#     nums.append([int(item) for item in input().split()])
    
# dp = [[None for j in range(m)] for i in range(n)]
# # path = [[None for j in range(m)] for i in range(n)]
# path_str = []

# dp[0][0] = dc(nums[0][0])
# # min = inf
# for i in range(1, m):
#     dp[0][i] = dp[0][i-1] + nums[0][i]

# for i in range(1, n):
#     for j in range(m):
#         tempmin = dp[i-1][0] + nums[i][0]    
#         tempsum = 0
#         for k in range(j, m):
#             tempsum2 = nums[i-1][k] + nums[i][k] + tempsum
#             tempmin = min(tempmin, tempsum2)
#             tempsum = dc(tempsum2)
#         if j == 0:    
#             dp[i][j] = dc(tempmin)
#         elif j == m-1:
#             dp[i][j] = min(dp[i-1][j], dp[i][j-1])
#         else:
#             dp[i][j] = min(dp[i][j-1], dp[i][j+1], dp[i-1][j])
            
            # if j == 0:
                
            # elif j == m-1:
                
            # else:    
        # dp = min()