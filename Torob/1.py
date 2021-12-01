def find_divisions(n: int):
    results = []
    for num in range(1, n + 1):
        if n % num == 0:
            results.append(num)
    return results



def is_nice_number(n: int):
    divisions = find_divisions(n)
    if sum(divisions) % 3 == 0:
        return True
    else:
        return False
    
    
def is_nice(n:int):
    divisions_sum = 0
    for number in range(1, n+1):
        if n % number == 0:
            divisions_sum += number
    return divisions_sum % 3 == 0
    
# print(find_divisions(10))
print(is_nice(10))