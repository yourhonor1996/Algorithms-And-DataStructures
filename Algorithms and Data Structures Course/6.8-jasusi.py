n = int(input())

corps_names = []
for i in range(n):
    corps_names.append(input())

corps = []
q = int(input())
for i in range(q):
    corps.append(input())
    
tempset = set()
count = 0
for item in corps:
    tempset.add(item)
    if(len(tempset)) == len(corps_names):
        count += 1
        tempset.clear()
        tempset.add(item)

print(count)
    
