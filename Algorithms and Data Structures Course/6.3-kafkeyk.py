from copy import deepcopy
n, k = [int(item) for item in input().split()]
nums = [int(item) for item in input().split()]

# nums.sort()

left = []
right = deepcopy(nums)

if k==1:
    print(max(nums))
    
if k==2:
    badi = max(nums)
    for i in range(len(nums)-1):
        left.append(right.pop(0))
        tempmin = min(max(left), max(right))
        if(tempmin < badi):
            badi = deepcopy(tempmin) 
    print(badi)
            
if k>=3:
    print(min(nums))
    
    