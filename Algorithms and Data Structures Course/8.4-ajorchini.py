q = int(input())
nums = []
for i in range(q):
    nums.append(int(input()))
    

ajors = [1,1,1,2]    
for i in range(4, int(1e5+1)):
    ajors.append(ajors[i-1] + ajors[i-2] + ajors[i-3] - ajors[i-4])
    
for number in nums:
    print(ajors[number] % int(1e9 + 7))