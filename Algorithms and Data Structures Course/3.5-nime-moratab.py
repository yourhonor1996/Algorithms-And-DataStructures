import copy
n = input()
nums = [int(item) for item in input().split()]


def newmethod400():
    def numof_differces(l1:list, l2:list):
        count = 0
        for  i in range(len(l1)):
            if l1[i] != l2[i]:
                count += 1
        return count
    return numof_differces

numof_differces = newmethod400()
        
    
    
def is_ascendable(lis:list):
    sorted_list = copy.deepcopy(lis)
    sorted_list.sort()
    if(numof_differces(lis, sorted_list) ==2):
        return 'YES'
    else: 
        return 'NO'
    
print(is_ascendable(nums))