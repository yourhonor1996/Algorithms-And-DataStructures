n, k = list(int(number) for number in  input().split())
list_of_nums = list(int(number) for number in input().split())

def make_new_hesabi(lis:list, i:int, step:int) -> list:
    # if i == len(lis)-1:
    #     return []
    a = lis[i]
    forwarNumber = len(lis)-i
    forward = list(range(a + step, a + forwarNumber*step,  step))
    bnackward = list(range(a - step, a - (i+1)*step, -step))
    bnackward.reverse()
    single = [a]
    return bnackward + single + forward     
    
def change_btw_lists(l1:list, l2:list):
    all_changes = []
    if len(l1) != len(l2):
        return None
    else:
        length = len(l1)
        for i in range(length):
            all_changes.append(abs(l2[i] - l1[i]))
    return sum(all_changes)
            
    
def num_of_changes(numbers:list, step:int):
    changes = []
    for i in range(len(numbers)-1):
        new_list = make_new_hesabi(numbers, i, step)
        # for item in 
        changes.append(change_btw_lists(numbers, new_list))
    
    return min(changes)
    # return changes

# for i in range(len(list_of_nums) - 1):
#     new_list = make_new_hesabi(list_of_nums, i, k)
#     print(new_list)
print(num_of_changes(list_of_nums, k))